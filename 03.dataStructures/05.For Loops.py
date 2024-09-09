websites = [
    "google.com",
    "airbnb.com",
    "twitter.com",
    "facebook.com",
    "amazon.com"
]

for element in websites:
    print(element)

print("===================================")
                                # for i in range(5):  # 0부터 4까지 반복
for i in range(len(websites)):  # 0 ~ (websites length - 1) 까지 반복
    print(websites[i])

print("===================================")
for index, value in enumerate(websites):
    print(f"Index: {index}, Value: {value}")