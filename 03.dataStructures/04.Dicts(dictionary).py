# key-value 구조
player = {
    "name"      : "wendy",
    'age'       : 31,
    "alive"     : True,
    'fav_food'  : ["chicken", "burger"]
} # single quote, double quote 아무거나 사용해도 됨

# 전체 출력
print(player)

# 데이터 가져오기
print(f"name        : {player["name"]}")
print(f"age         : {player["age"]}")
print(f"alive       : {player.get("alive")}")
print(f"fav_food    : {player.get("fav_food")}")

# 특정 key-value 삭제
player.pop("name")
player.pop("age")
print(player)

# 데이터 추가
player["point"] = 10000
player["city"]  = "seoul"
player["fav_food"].append("pizza")      # list형 value에 element 추가
player.get("fav_food").append("coke")   # list형 value에 element 추가
print(player)