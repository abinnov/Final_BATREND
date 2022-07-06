from emoji import UNICODE_EMOJI
import unidecode
import re

class clean_data():
    # remove URLs   
    def remove_URL(self,text):
        url = re.compile(r'https?://\S+|www\.\S+')
        return url.sub(r'',text)

    # remove htmls
    def remove_html(self,text):
        html=re.compile(r'<.*?>')
        return html.sub(r'',text)
    
    # remove punct
    def remove_punct(self,text):
        punc = '''!()[]{};:"\,<>./?@#$%^&*_~'''
        for ele in text:
            if ele in punc:
                text= text.replace(ele, "")
        return text

    # remove other ...
    def remove_other (self,text) : 
        text = text.rstrip()
        text = re.sub(' +', ' ', text)
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        return(text)

    # lower   
    def lower_text(self, text):
        return text.lower()

    # remove emojis
    def remove_emoji(self, text):
        to_replace = UNICODE_EMOJI["en"]
        result = text
        for x in to_replace:
            result = result.replace(x, "")
        return result

    # remove accents
    def remove_accents(self, text):
        return unidecode.unidecode(text)

    # clean text
    def clean(self,text) : 
        text = self.lower_text(text)
        text = self.remove_URL(text)
        text = self.remove_html(text)
        text = self.remove_punct(text)
        text = self.remove_other (text)
        text = self.remove_emoji(text)
        return text

