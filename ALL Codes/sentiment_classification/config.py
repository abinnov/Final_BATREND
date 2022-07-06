import warnings
warnings.filterwarnings('ignore')
import torch
from transformers import  AutoTokenizer, AutoModelForSequenceClassification
import os

model="philschmid/distilbert-base-multilingual-cased-sentiment"
#model="moussaKam/barthez-sentiment-classification"
path_to_finetuning_dt="/content/drive/MyDrive/Colab Notebooks/Sentiment_analysis/french_tweets.csv"
folder='/content/drive/MyDrive/sentiment_analysis'
folder_FT= os.path.join(folder , model+'_'+'fine_tuned') 
