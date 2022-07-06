from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch.nn.functional as F
from clean_data import clean_data
import sys
import config
import torch

def run(comment):

    comment=clean_data().clean(comment)
    model = AutoModelForSequenceClassification.from_pretrained(config.PRETRAINED_TOKENIZER)
    tokenizer = AutoTokenizer.from_pretrained(config.PATH)
    model.eval()
    test_encodings=tokenizer([comment], truncation=True, padding=True)
    print(test_encodings)  
    prediction_inputs = torch.tensor(test_encodings['input_ids'])
    prediction_masks = torch.tensor(test_encodings['attention_mask'])
    with torch.no_grad():
          outputs=model(input_ids=prediction_inputs, attention_mask=prediction_masks)
          predictions=F.softmax(outputs.logits, dim=1)
          # pred= torch.argmax(predictions, dim=1)
          # hna hoto li t7ébo les probabilités wili classe toul en fonction chnow t7bo 
          return predictions
    
if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])