import re
import string
import nltk 
nltk.download('stopwords')
from nltk.corpus import stopwords
stop = set(stopwords.words('french'))
class cleaner():
    #remove stop words
    def remove_stops(self,text) : 
        remove_stopwords = [w for w in text.split() if w not in stop]
        return ' '.join(remove_stopwords)

    # remove URLs   
    def remove_URL(self,text):
        url = re.compile(r'https?://\S+|www\.\S+')
        return url.sub(r'',text)

    # remove htmls
    def remove_html(self,text):
        html=re.compile(r'<.*?>')
        return html.sub(r'',text)

    def remove_emoji(self,text):
        emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)

    # remove punct
    def remove_punct(self,text):
        table=str.maketrans('','',string.punctuation)
        return text.translate(table)
    
    # remove other ...
    def remove_other (self,text) : 
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        return(text)

    def clean_dataFrame (self,df) : 
        for i in range(df.text.shape[0]):
            text = self.remove_stops(df.content[i])
            text = self.remove_URL(text)
            text = self.remove_other(text)
            df.text[i]=text
        return df
        
    def clean_text (self,text) : 
        
        text = self.remove_stops(text)
        text = self.remove_URL(text)
        text = self.remove_other(text)
            
        return text