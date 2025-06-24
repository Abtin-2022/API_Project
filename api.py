import nlpcloud
import os
import requests
url = "https://api.nlpcloud.io/v1/python-langdetect/langdetection" # nlp cloud language detection system
headers = {
    "Authorization": f"Token {os.environ.get('NLP_KEY')}",
    "Content-Type": "application/json",
}
data = {
    "text": "J'adore jouer au foot?"
}
response = requests.post(url, headers=headers, json=data)

print(response.json()) # returns list of languages denoted by their two character ISO code