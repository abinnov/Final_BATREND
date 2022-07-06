
from transformers import Trainer, TrainingArguments,DistilBertTokenizer,CamembertTokenizer,DistilBertForSequenceClassification
import torch
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.model_selection import train_test_split

# importing our classes 
from Dataset import Dataset
from Clean import *
from config import *

def compute_metrics(pred):
  labels = pred.label_ids
  preds = pred.predictions.argmax(-1)

  acc = accuracy_score(labels, preds)
  return {
      'accuracy': acc,

}

#----------------------------------
#       fine tuning function
#-----------------------------------
def fine_tuning(model_name,df,file):
  d= dict()
  comments= (df.text.values.tolist())
  labels=df.label.values.tolist()
  train_texts,test_texts,train_label,test_label= train_test_split(comments,labels,shuffle=True,test_size=0.2)
  try:
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
  except:
    model =DistilBertForSequenceClassification.from_pretrained(model_name)
  try:
    tokenizer = AutoTokenizer.from_pretrained(model_name,padding=True,truncation=True,max_length=132)
  except:
    try:
      tokenizer = CamembertTokenizer.from_pretrained(model_name,padding=True,truncation=True,max_length=132)
    except:
      tokenizer = DistilBertTokenizer.from_pretrained(model_name,padding=True,truncation=True,max_length=132)
  #train/test encoding     
  train_encodings= tokenizer(list(train_texts),truncation=True,padding=True,max_length=132)
  test_encoding=tokenizer(list(test_texts),truncation=True,padding=True,max_length=132)
  traindt = Dataset(train_encodings,train_label)
  testdt=Dataset(test_encoding,test_label)  
  training_args = TrainingArguments(
      output_dir=file,
      num_train_epochs=4,
      per_device_train_batch_size=32,
      per_device_eval_batch_size=32,
      warmup_steps=500,
      weight_decay=0.01,
      evaluation_strategy='epoch',
      logging_dir=file,

      learning_rate= 5e-3,
      logging_steps=80000,
      save_strategy="no"
  )
  
  trainer = Trainer(
      model=model,
      args=training_args,
      compute_metrics=compute_metrics,
      train_dataset=traindt,
      eval_dataset=testdt
      )
  trainer.train()
  #saving the model
  model.save_pretrained(file)
  tokenizer.save_pretrained(file)

def run():

  df= pd.read_csv(path_to_finetuning_dt)
  df_finetune =cleaner().clean_dataFrame(df)  
  fine_tuning(model,df_finetune ,folder_FT)

if __name__ == "__main__":
    run()