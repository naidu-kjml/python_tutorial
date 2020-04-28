import json

data ={ 
    'Personnes' : {
        'name':'said',
        'age':25,
        'wifes':[
            {'name':'safia','age': 22},
            {'name':'wejdan','age': 24},
            {'name':'oumaima','age': 25}
        ],
        'childrens':[
            {'name':'saffa','age': 2},
            {'name':'majed','age': 6},
            {'name':'imane','age': 4}
        ],
        'fonction':'Fekih',
        'hobies':['nikah','code','learning','doin']
    }
}

print(data['Personnes']['hobies'])
print(data['Personnes']['hobies'][0])

with open('json/file_data.json','w') as write_file :
    json.dump(data,write_file)


with open('json/file_data.json','r') as read_file :
    data1 = json.load(read_file)

print(data1)

data2 = json.load(open('json/file_data.json'))
print(data2)


