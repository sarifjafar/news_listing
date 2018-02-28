import requests

api_key = "get_your_own_key"
url = "https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey="+api_key


def print_news(articles,id):
	print("{id}) {title}\n BY:{by}\tDate:{date}\n{description}\n{url}"
		.format(id=id,title=str(articles["title"]),by=str(articles["author"]),date=str(articles["publishedAt"])
			,description=str(articles["description"]),url=str(articles["url"])))
	print("-------------------------------------------")

def get_news():
	res_json = requests.get(url).json()
	i = 1
	if str(res_json['status']) == 'ok':
		for articles in res_json["articles"]:
			print_news(articles,i)
			i = i + 1

get_news()	
