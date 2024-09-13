# Python Standard Library 가 아닌 인터넷에서 다운 받은 package import
# import requests --> 이렇게 import 해도 된다.

from requests import get

websites = [
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://amazon.com"
]

for website in websites:
    if not website.startswith("https://"):
        print(f"have to fix it ==> {website}")
        website = f"https://{website}"
        print(f"fixed it       ==> {website}")