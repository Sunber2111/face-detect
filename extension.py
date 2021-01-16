from flask_pymongo import PyMongo
from services.ai.VGG16 import Vgg16

mongo = PyMongo()
model_predict = Vgg16()
