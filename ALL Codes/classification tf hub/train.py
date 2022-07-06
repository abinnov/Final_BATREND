from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
import config
from clean_data import clean_data
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text

def run():
    df=pd.read_csv(config.TRAINING_FILE)
    # df['text'] = df['text'].apply(clean_data().clean)

    x_train , x_test , y_train , y_test =train_test_split(df['text'],df['label'],test_size=0.2, random_state=42, shuffle=True)

    label_as_binary = LabelBinarizer()
    train__y_labels = label_as_binary.fit_transform(y_train)
    #test__y_labels = label_as_binary.fit_transform(y_test)
 
    bert_preprocess = hub.KerasLayer("https://tfhub.dev/jeongukjae/smaller_LaBSE_15lang_preprocess/1")
    bert_encoder = hub.KerasLayer("https://tfhub.dev/jeongukjae/smaller_LaBSE_15lang/1")
   
    # Bert layers
    text_input = tf.keras.layers.Input(shape=(), dtype=tf.string, name='text')
    preprocessed_text = bert_preprocess(text_input)
    outputs = bert_encoder(preprocessed_text)

    # Neural network layers
    layer1 = tf.keras.layers.Dropout(0.1, name="dropout")(outputs['pooled_output'])
    layer2 = tf.keras.layers.Dense(9, activation='softmax', name="output")(layer1)

    # Use inputs and outputs to construct a final model
    model = tf.keras.Model(inputs=[text_input], outputs = [layer2])

    METRICS = [
      tf.keras.metrics.BinaryAccuracy(name='accuracy'),
      tf.keras.metrics.Precision(name='precision'),
      tf.keras.metrics.Recall(name='recall')
    ]
    model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=METRICS)
    for i in range(config.EPOCHS):
      model.fit(x_train, train__y_labels, epochs=1)
      PATH_TO_SAVE = f"/content/drive/MyDrive/Colab_Notebooks/classification_camembert_mariem/camembert500KW/Epoch_{i}"
      #model.evaluate(x_test, test__y_labels)
      model.save(PATH_TO_SAVE)
      model = tf.keras.models.load_model(config.SAVE_PATH)

