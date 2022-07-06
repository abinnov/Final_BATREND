from transformers import Trainer, TrainingArguments, AutoTokenizer, AutoModelForSequenceClassification
from sklearn.model_selection import train_test_split
import pandas as pd
from dataset import Dataset 
import config
from sklearn.metrics import accuracy_score
# from clean_data import clean_data
from tqdm import tqdm 
def compute_metrics(pred):
  labels = pred.label_ids
  preds = pred.predictions.argmax(-1)
  acc = accuracy_score(labels, preds)
  return {'accuracy': acc,}

def run():
    df=pd.read_csv(config.TRAINING_FILE)
    df.dropna(subset=['text'],inplace=True)
    # comments=[]
    # for comment in df.text.tolist():
    #     comments.append(clean_data().clean(comment))
    X_train = df.text.tolist()
    y_train = df.label.tolist()

    test=pd.read_csv(config.TEST_FILE)
    test.dropna(subset=['text'],inplace=True)
    X_test = test.text.tolist()
    y_test = test.label.tolist()

    model=AutoModelForSequenceClassification.from_pretrained(config.PRETRAINED_MODEL, num_labels=9)
    tokenizer=AutoTokenizer.from_pretrained(config.PRETRAINED_TOKENIZER)
    
    model.train() 
    train_encodings=tokenizer(X_train, truncation=True, padding=True)
    val_encodings=tokenizer(X_test, truncation=True, padding=True)
    train_dataset=Dataset(train_encodings, y_train)
    val_dataset=Dataset(val_encodings, y_test)
    
    training_args=TrainingArguments(
    output_dir=config.OUTPUT_DIR,
    num_train_epochs=1,
    per_device_train_batch_size=config.TRAIN_BATCH_SIZE,
    per_device_eval_batch_size=config.VAL_BATCH_SIZE,
    warmup_steps=config.WARMUP_STEPS,
    learning_rate=config.LEARNING_RATE,
    weight_decay=config.WEIGHT_DECAY,
    logging_dir=config.LOGGING_DIR,
    logging_steps=config.LOGGING_STEPS,
    evaluation_strategy='epoch',
    save_strategy="no"
    )
    print ('Training ')
    for i in tqdm(range(1,config.NUM_EPOCHS)) : 
      trainer = Trainer(
          model=model,
          args=training_args,
          compute_metrics=compute_metrics,
          train_dataset=train_dataset,
          eval_dataset=val_dataset
          )
      trainer.train()
      PATH_TO_SAVE = f"/content/drive/MyDrive/Colab_Notebooks/classification_camembert/epochs/Epoch_{i}"
      model.save_pretrained(PATH_TO_SAVE)
      model = AutoModelForSequenceClassification.from_pretrained(PATH_TO_SAVE)

if __name__ == "__main__":
    run()