import rest_api_routes

new_user = {
        "user_name": "DJ",
        "user_password": "1234"
        }


#response = rest_api_routes.add_user(new_user)
response = rest_api_routes.get_user('Amit')
print(f'{response}')
