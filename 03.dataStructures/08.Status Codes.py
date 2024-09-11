from requests import get

websites = [
    "https://google.com",
    "https://airbnb.com",
    "https://twitter.com",
    "https://facebook.com",
    "https://amazon.com"
]

# dictionary
results = {}

for website in websites:
    response = get(website)

    print(response)
    print(f"status_code : {response.status_code}")
    
    if(response.status_code == 200):
        results[website] = "OK"
    else:
        results[website] = "BAD"

print(results)