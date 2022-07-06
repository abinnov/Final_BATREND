import pandas as pd 
from Config import *
import torch 
def read_csv(path): 
    df = pd.read_csv(path)
    df.dropna(subset=['text'],inplace=True)
    return df 
def khawi_data(df) : 
    # df.drop('Unnamed: 0',axis=1 ,inplace=True ) 
    df = pd.concat([df[:2],df[102:104] , df[202:204] , df[302:304] , 
    df[402:404] ,df[502:504]  , df[602:604]]).reset_index().drop('index',axis=1)
    df.columns = [ 'text','category']
    df['category'] = df['category'].map(LABELS_MAP)
    return df 


def save_checkpoint(state, PATH):
    print("=> Saving checkpoint")
    torch.save(state, PATH)


