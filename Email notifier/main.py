import requests
from send_email import send_email

api = "5ffb75ccde1b49a4ae6d7f2e0d29cfbf"
url = "https://newsapi.org/v2/everything?" \
      "q=tesla&" \
      "from=2025-12-08&sortBy=publishedAt&" \
      "apiKey=5ffb75ccde1b49a4ae6d7f2e0d29cfbf"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and descriptions
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n"\
               + article["description"] + "\n"\
               + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)