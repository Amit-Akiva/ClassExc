import requests

user_bod = {
        "user_name": "Amit",
        "user_password": "1234"
        }
response = requests.request('POST' ,url="http://127.0.0.1:3002/users/add_user" ,json=user_bod)
print(f'{response.json()}')

user_amit = {
        "user_name": "Amit"
}

response = requests.request('GET' ,url="http://127.0.0.1:3002/users/get_user" ,params=user_amit)
#response = requests.request('GET' ,url = "http://127.0.0.1:9090/users/get_user" ,params={'user_name': connexion.request.args['Amit']})
print(f'{response.json()}')

Song_Add = {
        "song_genre": "Rock",
        "song_performer": "Creedence Clearwater Revival",
        "song_title": "Run Through the Jungle",
        "song_year": 1970
}

response = requests.request('POST' ,url="http://127.0.0.1:9090/songs/add_song" ,json=Song_Add)
print(f'{response.json()}')