#post detayları, header

import requests
import json

"""
#GET
user_input = input("Enter ID: ")
url = f"https://jsonplaceholder.typicode.com/todos/{user_input}" #1.yi getirir

get_response = requests.get(url)
print(get_response.json())
"""

#POST
to_do_item = {
    "userId": 2,
    "title": "my to do",
    "completed": False
}

post_url = "https://jsonplaceholder.typicode.com/todos"

#optional header
headers = {"content-Type":"application/json"}
#post_response = requests.post(post_url,json=to_do_item,headers=headers) #json parametresini data olarak değil json olarak yollamalısın
#print(post_response.json())
#print(post_response.json()) #sunucu hatası,datayı jsona çevirince düzeldi
#db e ekleme yapmamış olma ihtimali var
#print(json.dumps(to_do_item))#bir şey değişmez ancak artık bu bir json, sözlük değil
post_response = requests.post(post_url,data=json.dumps(to_do_item),headers=headers) #oldu
print(post_response.json())