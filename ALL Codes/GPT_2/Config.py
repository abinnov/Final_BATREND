from transformers import GPT2Model
hidden_size=768 
max_seq_len=20
gpt_model_name="gpt2"
SAVE_PATH = '/content/drive/MyDrive/gpt_2.pt'

# Labels : 
LABELS = {'economie':0,'environnement':1,'immigration':2,
           'laicite':3,'sante':4,'sécurité':5,'autre':6}


LABELS_MAP = {0:'economie',1:'environnement',2:'immigration',
           3:'laicite',4:'sante',5:'sécurité',6:'autre'}
           
num_classes=7

# à Changer si un pb fl résultuts  : 
PATH = '/content/drive/MyDrive/Trend_analysis/Datasets/Topics/Test_7classes.csv' # data finetunning 
EPOCHS = 1
LR = 1e-5
COMMENT = " L'économie française "
