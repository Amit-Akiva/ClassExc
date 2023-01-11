from infrastructure import get_users_info
from logic import verify_methods
import rest_api_routes

f = get_users_info.load_user_data('C:/Users/amitak/PycharmProjects/song-server/users.json')
names_in_data = get_users_info.names(f)
desired_keys_json = ['password', 'name', 'friends', 'playlists']
desired_keys_server = ['user_name', 'friends', 'playlists']
undesired_key_server = 'password'

new_user = {
        "user_name": "_DJ",
        "user_password": "1234"
        }


def test_names():
    ret_val = verify_methods.unique_names(names_in_data)
    return ret_val


# From users.json data base - requirement 2
def missing_fields():
    lis = list()
    for i in names_in_data:
        for j in desired_keys_json:
            if not(verify_methods.fields_exist(f.get(i), j)):
                lis.append(i + j)
    return lis


# Data from server - requirement 11 to verify user data
def user_fields_server():
    lis = list()
    for i in names_in_data:
        if verify_methods.fields_exist(rest_api_routes.get_user(i).get('data'), undesired_key_server):
            lis.append(i + undesired_key_server)
        for j in desired_keys_server:
            if not (verify_methods.fields_exist(rest_api_routes.get_user(i).get('data'), j)):
                lis.append(i + j)
    return lis
