from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline

# Load pre-trained BERT model and tokenizer
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Use pipeline to simplify prediction
#classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Test with example sentences
text1 = "I love this product! It's amazing."
text2 = "You are good at eating Shit. "

# Get predictions
result1 = classifier(text1)
result2 = classifier(text2)

print("Text 1:", result1)
print("Text 2:", result2)