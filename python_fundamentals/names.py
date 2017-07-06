def print_names(listlib):
    for x in listlib:
        print x['first_name'], x['last_name']

def print_names_too(listlib):
    count=1
    for x in listlib:
        print "%d - " % count,
        print x['first_name'], x['last_name'],
        print " - %s" % (len(x['first_name'])+ len(x['last_name']))
        count += 1




students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

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
#print_names(students)

for key in users:
    print key
    print_names_too(users[key])