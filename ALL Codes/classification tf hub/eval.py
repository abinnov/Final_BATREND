import tensorflow as tf
import config
import pandas as pd
from sklearn.preprocessing import LabelBinarizer
#import sys
label_as_binary = LabelBinarizer()
model = tf.keras.models.load_model(config.SAVE_PATH)
test=pd.read_csv(config.TEST_FILE)
x_test=test[['text']]
y_test=test[['label']]
test_y_labels = label_as_binary.fit_transform(y_test)

model.evaluate(x_test, test_y_labels)
