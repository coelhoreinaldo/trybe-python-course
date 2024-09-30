from parsel import Selector
import requests


URL_BASE = "http://books.toscrape.com/catalogue/"
next_page_url: str | None = "page-1.html"
while next_page_url:
    response = requests.get(URL_BASE + next_page_url)
    selector = Selector(text=response.text)
    for product in selector.css(".product_pod"):
        # Get the title and price of the book
        # title = product.css("h3 a::attr(title)").get()
        # price = product.css(".price_color::text").get()
        # print(title, price)

        # Get the details of the book
        detail_href = product.css("h3 a::attr(href)").get() or ""
        detail_page_url = URL_BASE + detail_href

        detail_response = requests.get(detail_page_url)
        detail_selector = Selector(text=detail_response.text)

        description = detail_selector.css("#product_description ~ p::text").get()
        print(description)

    next_page_url = selector.css(".next a::attr(href)").get()
