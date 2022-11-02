import requests

API_KEY = "4f4b02fc71b8492d89c453b80a864890"

def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey="+API_KEY
    news = requests.get(main_url).json()
    # print(news)
    article = news['articles']

    news_article = []

    for ar in article:
        news_article.append(ar['title'])

    for i in range(5):
        print(i+1, news_article[i])

if __name__ == '__main__':
    news()