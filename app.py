import json

student = '{"name": "Anurag", "email": "anurag.nandigama@montrealcollege.ca", "language": ["English", "Telugu"]}'

student_dict = json.loads(student)

# print(student_dict)
# print(type(student_dict))
# print(student_dict['name'])

#student_json = json.dumps(student_dict)

#print(student_json)


with open('./student.json') as f:
    data = json.load(f)


with open('./stripe_sample.json') as f:
    strip_data = json.load(f)

# print(data)
# print(type(data))

print(strip_data)