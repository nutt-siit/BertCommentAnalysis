from itertools import islice
from youtube_comment_downloader import *
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline

# Bert setting
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

#Youtube API setting
downloader = YoutubeCommentDownloader()
#snow white official trailer
comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=iV46TJKL8cU&t=5s', sort_by=SORT_BY_POPULAR)


#for comment in comments:
print('--------------------------------------')
for comment in islice(comments, 5):
    text_comment = comment['text']
    result = classifier(text_comment)
    print(comment['text'])
    print(result)
    print('--------------------------------------')