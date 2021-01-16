import face_recognition
from glob import glob
import cv2
import pandas as pd
from PIL import Image
import numpy as np
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications import imagenet_utils
from sklearn import metrics
import sklearn
import pickle
from PIL import Image
from sklearn import preprocessing
import base64
from scipy import ndimage

class Vgg16:

    def __init__(self):

        self.le = preprocessing.LabelEncoder()

        self.le.fit(['5f74a5639d109007b0010bae', '5f74a5f79d109007b0010baf', '5f74a5f79d109007b0010bb0',
                     '5f74a5f79d109007b0010bb1', '5f74a63f9d109007b0010bb2', '5f74a63f9d109007b0010bb3'])

        self.model_detect = VGG16(weights='imagenet', include_top=False)

    def detect(self, base64_string, acc_id):
        
        self.model_log = pickle.load(open('./services/models/'+acc_id+'.pickle', 'rb'))

        nparr = np.fromstring(base64.b64decode(base64_string), np.uint8)

        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        all_faces_locations = face_recognition.face_locations(img, model='hog')

        for current_face in all_faces_locations:

            top, right, bot, left = current_face

            current_face_img = gray[top:bot, left:right]

            size = current_face_img.shape[0]

            if size >= 224:
                gray_re = cv2.resize(current_face_img, (224, 224), cv2.INTER_AREA)
            else:
                gray_re = cv2.resize(current_face_img, (224, 224), cv2.INTER_CUBIC)
            
            input_img = cv2.cvtColor(gray_re,cv2.COLOR_GRAY2RGB)

            gray_re = np.expand_dims(input_img, 0)

            gray_re = imagenet_utils.preprocess_input(gray_re)

            data_pre = np.vstack(gray_re)

            features = self.model_detect.predict(np.array([data_pre]))

            features = features.reshape((features.shape[0], 512*7*7))

            results = self.model_log.predict(features)[0]

            if results == 1:
                return 1

        return 0

    def res_img(self, image):
        image = cv2.resize( image, (224, 224), cv2.INTER_AREA)
        image = np.expand_dims(image, 0) 
        image = imagenet_utils.preprocess_input(image)
        return image

    def get_features_face(self, base64_strings):

        arr_image = []

        for ind in base64_strings:
            base64_string = base64_strings[ind].split(",")[1]
            nparr = np.fromstring(base64.b64decode(base64_string), np.uint8)

            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

            all_faces_locations = face_recognition.face_locations(
                img, model='hog')

            arr_face = []

            top, right, bot, left = all_faces_locations[0]

            current_face_img = img[top:bot, left:right]

            size = current_face_img.shape[0]

            scale_percent = 160

            # calculate the 50 percent of original dimensions
            width = int(current_face_img.shape[1] * scale_percent / 100)

            height = int(current_face_img.shape[0] * scale_percent / 100)

            dsize = (width, height)

            # resize image
            img_scale_160 = cv2.resize(current_face_img, dsize)

            quarter_height, quarter_width = height / 4, width / 4

            T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

            img_translation = cv2.warpAffine(
                current_face_img, T, (width, height))

            face_flip = cv2.flip(current_face_img, 90)

            rotated = ndimage.rotate(current_face_img, 20)

            light_img = current_face_img + 20

            dark_img = current_face_img - 20

            if size >= 224:
                gray_re = cv2.resize(
                    current_face_img, (224, 224), cv2.INTER_AREA)
            else:
                gray_re = cv2.resize(
                    current_face_img, (224, 224), cv2.INTER_CUBIC)

            gray_re = np.expand_dims(gray_re, 0)

            gray_re = imagenet_utils.preprocess_input(gray_re)
            face_flip = imagenet_utils.preprocess_input(face_flip)
            rotated = imagenet_utils.preprocess_input(rotated)
            img_scale_160 = imagenet_utils.preprocess_input(img_scale_160)
            img_translation = imagenet_utils.preprocess_input(img_translation)
            light_img = imagenet_utils.preprocess_input(light_img)
            dark_img = imagenet_utils.preprocess_input(dark_img)

            # arr_image.append(self.res_img(gray_re))
            arr_image.append(self.res_img(face_flip))
            arr_image.append(self.res_img(rotated))
            arr_image.append(self.res_img(img_scale_160))
            arr_image.append(self.res_img(img_translation))
            arr_image.append(self.res_img(light_img))
            arr_image.append(self.res_img(dark_img))

        arr_image = np.array([x for x in arr_image])
        data_X =  np.vstack(arr_image)

        features = self.model_detect.predict(data_X)

        features = features.reshape((features.shape[0], 512*7*7))

        return features

    def training_new_face(self, base64_strings, userid):
        self.le.fit([userid])
        id_model_detect = self.le.transform([userid])[0]
        arr_features = []
        x = self.get_features_face(base64_strings)
        print(x.shape)
        x = np.concatenate((x,[np.ones(7*7*512)]))
        print(x.shape)
        y = np.ones(len(base64_strings)*6)*id_model_detect
        y = np.append(y, np.array([100000]))
        print(y)
        self.model_log.partial_fit(x, y)
        pickle.dump(self.model_log, open(
            './services/models/model_test.pickle', 'wb'))
        return id_model_detect
    
    def detect_test(self, base64_string):

        self.model_log_test = pickle.load(open('./services/models/model_test.pickle', 'rb'))

        nparr = np.fromstring(base64.b64decode(base64_string), np.uint8)

        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        all_faces_locations = face_recognition.face_locations(img, model='hog')

        for current_face in all_faces_locations:

            top, right, bot, left = current_face

            current_face_img = img[top:bot, left:right]

            size = current_face_img.shape[0]

            if size >= 224:
                gray_re = cv2.resize(
                    current_face_img, (224, 224), cv2.INTER_AREA)
            else:
                gray_re = cv2.resize(
                    current_face_img, (224, 224), cv2.INTER_CUBIC)

            gray_re = np.expand_dims(gray_re, 0)

            gray_re = imagenet_utils.preprocess_input(gray_re)

            data_pre = np.vstack(gray_re)

            features = self.model_detect.predict(np.array([data_pre]))

            features = features.reshape((features.shape[0], 512*7*7))

            results = self.model_log_test.predict_proba(features)[0]
            
            print(results)
            if results.argmax() == 1:
                return 1

        return 0


