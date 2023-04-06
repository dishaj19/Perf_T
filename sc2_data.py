user = {1: {
    "username": "aaa",
    "password": "aaa@1"
}, 2: {
    "username": "bbb",
    "password": "bbb@1"
}, 3: {
    "username": "ccc",
    "password": "ccc@1"
}, 4: {
    "username": "ddd",
    "password": "ddd@1"
}, 5: {
    "username": "eee",
    "password": "eee@1"
}, 6: {
    "username": "fff",
    "password": "fff@1"
}, 7: {
    "username": "ggg",
    "password": "ggg@1"
}, 8: {
    "username": "hhh",
    "password": "hhh@1"
}, 9: {
    "username": "iii",
    "password": "iii@1"
}, 10: {
    "username": "jjj",
    "password": "jjj@1"
}
}
import json

s = json.dumps(user)

with open('user_data_in_text.txt', "w") as f:
    f.write(s)
