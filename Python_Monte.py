import json

#Create the first data dictionary
poop = {
    'name': 'Praman',
    'age': '9,204 days',
    'city': 'Seattle',
    'interests': ['Traveling', 'Gaming', 'Collecting', 'Pokemon'],
    'is_student': True
}

#Write data to poop.json
with open('poop.json', 'w') as json_file:
    json.dump(poop, json_file, indent=4)
                      
print('Data has been written to poop.json')

#Read data from poop.json
with open('poop.json', 'r') as json_file:
    loaded_data = json.load(json_file)                

print("Successfully able to read poop.json")
print(loaded_data)

#Create the second data dictionary
poop2 = {
    'name': 'Osama Bin Ballin',
    'age': '9,204 days',
    'city': 'Twin Skyscrapers',
    'interests': ['Traveling', 'Bombsquad', 'Ballin', 'History'],
    'is_student': False
}

#Write data to poop2.json
with open('poop2.json', 'w') as json_file:
    json.dump(poop2, json_file, indent=4)
                      
print('Data has been written to poop2.json')

#Read data from poop2.json
with open('poop2.json', 'r') as json_file:
    loaded_data2 = json.load(json_file)                

print("Successfully able to read poop2.json")
print(loaded_data2)