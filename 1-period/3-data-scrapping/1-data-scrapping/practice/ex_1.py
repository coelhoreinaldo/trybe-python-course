import requests

text = requests.get("https://httpbin.org/encoding/utf8").text

print(text)
