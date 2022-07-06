#train
# les params à changer : 
TRAINING_FILE = '/content/drive/MyDrive/Colab_Notebooks/classification_camembert_mariem/train500KW.csv'
TEST_FILE = '/content/drive/MyDrive/Colab_Notebooks/classification_camembert_mariem/test500KW.csv'
PATH = '/content/drive/MyDrive/Colab_Notebooks/classification_camembert/epochs/Epoch_3'

# .........
PRETRAINED_MODEL = 'camembert-base'
PRETRAINED_TOKENIZER = 'camembert-base'
OUTPUT_DIR="./"
NUM_EPOCHS=4
TRAIN_BATCH_SIZE=16
VAL_BATCH_SIZE=64
WARMUP_STEPS=500
LEARNING_RATE=5e-5
WEIGHT_DECAY=0.01
LOGGING_DIR='./logs'
LOGGING_STEPS=20

