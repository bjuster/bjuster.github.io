import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "f7c260e964mshc8f0dc2aeab6664p194041jsnebdcb4c582a7"
    }

response = requests.request("GET", url, headers=headers)

response_data = response.json()
#print(response_data)
#print(response_data["response"])

country_data = response_data["response"]




#print(country_data[0]["cases"])


#country_num = len(country_data)
#for country in country_data:
    #for num in range(country_num):
        #print(country_data[num]["cases"])

country_data_dict = {}
print(country_data)
for countries in country_data:
    print(countries['country'])
    print(countries['cases'])
    print(countries['deaths'])

with open('data.json', 'w') as file:
    json.dump(country_data,file, indent = 4)


if response.status_code == 200:
    print('\n-------------Updated JSON file successfully-----------')

else:
    print('Got an error.')
