websites = [
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://amazon.com"
]

for website in websites:
    print("========================================")
    if not website.startswith("https://"): # not --> !(논리부정 연산자) 역할
        print(f"have to fix it ==> {website}")
        website = f"https://{website}"
        print(f"fixed it       ==> {website}")
    else:
        print(f"good to go     ==> {website}")
    print("========================================")