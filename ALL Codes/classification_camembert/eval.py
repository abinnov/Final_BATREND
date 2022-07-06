from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.utils.data import DataLoader
import torch
import torch.nn.functional as F
import pandas as pd
from dataset import Dataset 
import config
# from clean_data import clean_data

def run():
    tokenizer=AutoTokenizer.from_pretrained(config.PRETRAINED_TOKENIZER)
    model = AutoModelForSequenceClassification.from_pretrained(config.PATH)
    model.eval()

    df=pd.read_csv(config.TEST_FILE)
    df.dropna(subset=['text'],inplace=True)

    # comments=[]
    # for comment in df.text.tolist():
    #     comments.append(clean_data().clean(comment))
    comments = df.text.tolist()
    labels=df.label.tolist()

    test_encodings=tokenizer(comments, truncation=True, padding=True)
    test_dataset=Dataset(test_encodings, labels) 

    accuracy = 0.0
    total = 0.0
    test_loader=DataLoader(test_dataset, batch_size=16, shuffle=True)    
    with torch.no_grad():
        for batch in test_loader:
            input_ids=batch['input_ids']
            attention_mask=batch['attention_mask']
            labels=batch['labels']
            outputs=model(input_ids, attention_mask=attention_mask, labels=labels)
            predictions=F.softmax(outputs.logits, dim=1)
            pred= torch.argmax(predictions, dim=1)
            total += labels.size(0)
            accuracy += (pred == labels).sum().item()
        accuracy = (100 * accuracy / total)
    print(accuracy)
    return accuracy

if __name__ == "__main__":
    run()