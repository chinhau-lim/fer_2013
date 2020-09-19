import numpy as np 
import tensorflow as tf 
from tensorflow.keras.models import model_from_json

config = tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.15
sess = tf.compat.v1.Session(config=config)

class FacialExpressionModel(object):

	EMOTIONS = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

	def __init__(self, json_file, weights_file):

		with open(json_file, "r") as j_file:
			loaded_model_json = j_file.read()
			self.loaded = model_from_json(loaded_model_json)

		self.loaded.load_weights(weights_file)
		#self.loaded.make_predict_function()

	def predict_emotion(self, img):
		self.preds = self.loaded.predict(img)
		return FacialExpressionModel.EMOTIONS[np.argmax(self.preds)]
