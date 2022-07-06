from config.py import *
from transformers import pipeline
from Clean import *
import sys

model = AutoModelForSequenceClassification.from_pretrained(folder_FT)
tokenizer = AutoTokenizer.from_pretrained(folder_FT) 
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer,max_length=132,truncation=True)

def TEST_distilbert(comment):
    comment =cleaner().clean_text(comment)
    model = AutoModelForSequenceClassification.from_pretrained("/content/drive/MyDrive/data/cardiffnlp/twitter-xlm-roberta-base-sentiment_fine_tune_1")
    tokenizer = AutoTokenizer.from_pretrained("/content/drive/MyDrive/data/cardiffnlp/twitter-xlm-roberta-base-sentiment_fine_tune_1")  
    classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
    results=classifier(comment)
    return(results['label'])
# def get_sentiment(comment):
#     comment =cleaner().clean_text(comment)

    # result=classifier(comment)
    # if result[0]['label']=='Positive' and result[0]['score']>0.7:
    #     return result[0]['score'], 1
    # elif result[0]['label']=='Negative' and result[0]['score']>0.7:
    #     return result[0]['score'], 0
    # else:
    #     return result[0]['score'], 2
    
if __name__ == "__main__":
    TEST_distilbert(sys.argv[1])