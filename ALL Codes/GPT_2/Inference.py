from unicodedata import name
from Config import *
import torch 
from model import *

def Inference (model_new,comment,tokenizer) : 
    # model_new.eval()
    # fixed_text = " ".join(comment.lower().split()) # EL preprocess el lézm 
    fixed_text = comment 
    model_input = tokenizer(fixed_text, padding='max_length', max_length=20, truncation=True, return_tensors="pt")
    mask = model_input['attention_mask'].cpu()
    input_id = model_input["input_ids"].squeeze(1).cpu()
    output = model_new(input_id, mask)
    prob = torch.nn.functional.softmax(output, dim=1)[0]
    pred_label = LABELS_MAP[output.argmax(dim=1).item()]
    return pred_label


model_new = SimpleGPT2SequenceClassifier(hidden_size=768, num_classes=7, max_seq_len=20, gpt_model_name="gpt2")
# model_new = model_new.load_state_dict(torch.load(SAVE_PATH)["state_dict"])
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenizer.padding_side = "left"
tokenizer.pad_token = tokenizer.eos_token
print(Inference (model_new,COMMENT,tokenizer))
