import torch 
from torch import nn 
from tqdm import tqdm 
from Dataset import *
from torch.optim import Adam
from Utils import * 
from model import *
from Config import * 
import numpy as np 
import pandas as pd 
def train(model, train_data, learning_rate, epochs):    
    print('Step 1 : Loading GPT ')
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokenizer.padding_side = "left"
    tokenizer.pad_token = tokenizer.eos_token
    print('Step 2 : Creating Dataset ')
    train= Dataset(train_data,tokenizer)
    print('Step 3 : Creating Dataloader  ')

    train_dataloader = torch.utils.data.DataLoader(train, batch_size=2, shuffle=True)
    # val_dataloader = torch.utils.data.DataLoader(val, batch_size=2)
    
    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    
    criterion = nn.CrossEntropyLoss()
    optimizer = Adam(model.parameters(), lr=learning_rate)
    
    if use_cuda:
        model = model.cuda()
        criterion = criterion.cuda()
    for epoch_num in range(epochs):
        print('Step 3 : Running An Epoch ')
        total_acc_train = 0
        total_loss_train = 0
        
        for train_input, train_label in tqdm(train_dataloader):
            print('Step 4 : Forwording a Batch ')
            train_label = train_label.to(device)
            mask = train_input['attention_mask'].to(device)
            input_id = train_input["input_ids"].squeeze(1).to(device)
            model.zero_grad()
            output = model(input_id, mask)
            batch_loss = criterion(output, train_label)
            total_loss_train += batch_loss.item()
            acc = (output.argmax(dim=1)==train_label).sum().item()
            total_acc_train += acc
            batch_loss.backward()
            optimizer.step()

        print('Step 5 : Saving State ')
        model.load_state_dict(model.state_dict())
        fixed_text = 'je suis en bonne santé hamdellah' 
        model_input = tokenizer(fixed_text, padding='max_length', max_length=20, truncation=True, return_tensors="pt")
        mask = model_input['attention_mask'].cpu()
        input_id = model_input["input_ids"].squeeze(1).cpu()
        output = model(input_id, mask)
        prob = torch.nn.functional.softmax(output, dim=1)[0]
        pred_label = LABELS_MAP[output.argmax(dim=1).item()]
        print(pred_label)



            

df = khawi_data(read_csv(PATH))
# df_train, df_val, df_test = np.split(df.sample(frac=1, random_state=35),
#                                         [int(0.8*len(df)), int(0.9*len(df))])
model = SimpleGPT2SequenceClassifier(hidden_size=768, num_classes=num_classes, max_seq_len=20, gpt_model_name="gpt2")


train(model, df, LR, EPOCHS)

