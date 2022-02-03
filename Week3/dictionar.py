my_dictionary = {
    'integer': 5,
    'string': "eu",
    'float': 3.5,
    'boolean': True
}

print(my_dictionary['float'])
print(my_dictionary.get('string'))
print(my_dictionary.keys())  # afisam cheile din dictionar
my_dictionary.update({  # adaugam valori noi
    'number': 45,
    'altceva': 'nu stiu ce'
})
print(my_dictionary.keys())

for k, v in my_dictionary.items():
    if k == 'boolean':
        print(f"Key: {k}")
        print(f"Value: {v}")

my_dict = {
    'users': [
        {
            'username': 'Diana',
            'password': '1234ds',
            'email': 'serbdiana11@gmail.com'
        },
        {
            'username': 'Mihai',
            'password': '1234mc',
            'email': 'mihaicadis@gmail.com',
        },
        {
            'username': 'Ileana',
            'password': '1234is',
            'email': 'ileanaserb@gmail.com',
            'home': ['Brasov', 'Lalelelor', 4]
        }
    ],
    'admin': {
        'user': 'admin1',
        'password': 'asdf1234'
    }
}

print(my_dict['users'][2]['home'][0])  # afisare Brasov

for k, v in my_dict.items():
    if k == 'users':
        for user in v:
            for k2, v2 in user.items():
                if k2 == 'home':
                    print(v2[0])