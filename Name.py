
# Part One

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# for x in students:
#     print x['first_name'], x['last_name']
#

# Part Two

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

num=0
for key, data in users.items():
     #print data
     for value in data:
         num += 1
         print num,value['first_name'], value['last_name'], len(value['last_name'])+len(value['first_name'])







# for s in students:
#     print x['first_name'], x['last_name']
#
#
# for i in Instructors:
#     print x['first_name'], x['last_name']
