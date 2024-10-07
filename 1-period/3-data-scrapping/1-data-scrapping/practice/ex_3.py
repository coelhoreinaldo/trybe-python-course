import requests

response = requests.get(
    "https://scrapethissite.com/pages/advanced/?gotcha=headers",
    headers={"User-Agent": "Chrome"},
)

assert (
    "User-Agent value doesn't look like a standard mozilla/chrome/safari value"
    not in response.text
)
