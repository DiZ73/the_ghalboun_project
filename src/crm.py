import io, json

with open('contacts.json') as data_file:
 data = json.load(data_file)
print(data)

data['contacts'].append({"firstname":"Ramzi","lastname":"Rizk","DOB":"09-20-1982"})

print(data)

with io.open('contacts.json', 'w', encoding='utf-8') as f:
 f.write(unicode(json.dumps(data, ensure_ascii=False)))