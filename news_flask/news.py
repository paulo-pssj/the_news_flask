import requests

from flask import render_template, redirect, request, url_for
from app import app

@app.route('/')
def index():
    news_key = 'SUA API KEY'
    url = f'https://newsapi.org/v2/top-headlines?country=br&pageSize=100&apiKey={news_key}'
    data = requests.get(url).json()
    news = []
    for id, _ in enumerate(data['articles']):
        new = {
        'fonte': data['articles'][id]['source']['name'],
        'autor': data['articles'][id]['author'],
        'titulo': data['articles'][id]['title'],
        'image': data['articles'][id]['urlToImage'],
        'descricao': data['articles'][id]['description'],
        'criado_em': data['articles'][id]['publishedAt'],
        'url': data['articles'][id]['url']
        }
        news.append(new)
    
    return render_template('index.html', news=news)
    


