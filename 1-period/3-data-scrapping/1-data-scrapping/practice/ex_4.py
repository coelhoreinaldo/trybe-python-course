from parsel import Selector
import requests

URL_BASE = "http://books.toscrape.com/catalogue/"
response = requests.get(URL_BASE + "a-light-in-the-attic_1000/index.html")
selector = Selector(text=response.text)

name = selector.css(".product_main h1::text").get()
price = selector.css(".product_main .price_color::text").re_first(r"£\d+\.\d{2}")
image_url = URL_BASE + selector.css("#product_gallery img::attr(src)").get()

description = selector.css("#product_description ~ p::text").get()
suffix = "...more"

if description and description.endswith(suffix):
    description = description[: -len(suffix)]

available_books = selector.css(".instock.availability").re_first(r"\d+")

result = f"{name}, {price}, {description}. {image_url}, {available_books}."

print(result)
