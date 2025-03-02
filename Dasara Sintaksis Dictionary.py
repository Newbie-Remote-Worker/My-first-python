user = {
    'id': 1012731,
    'name': 'Robert Davis Chaniago',
    'username': 'Robertdavgo',
    'email': 'robertdago@rocketmail.com',
    'pass': 'Robertshimself31523',
    'address': {
        'street': 'jln. H. Misar',
        'city': 'Jakarta Timur',
        'zipcode': '13770',
    }
}

print(user)
print(id)
print(user['name'])
print(user['username'])
print(user['email'])
print(user['pass'])
print(user['address']['street'])
print(user['address']['city'])
print(user['address']['zipcode'])
print(type(user))

print('\nChange Dictionary to JSON')
import json
result = json.dumps(user)
print(type(result))
print(result)

with open('result.json', 'w') as file:
json.dump(user, file)




