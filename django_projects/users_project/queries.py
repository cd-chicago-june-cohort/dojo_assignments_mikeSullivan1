import django
from apps.dojo_ninjas.models import *

# b = User.objects.get(id=3)
# b.last_name = "Pelican"
# b.save()

#User.objects.get(id=4).delete()
# print b.first_name, b.last_name, b.email


# all_dojos = Dojo.objects.all()
# for dojo in all_dojos:
#      print dojo.name,dojo.city,dojo.state

# seattle = Dojo.objects.filter(city="Seattle")

# Ninja.objects.create(first_name = "new", last_name = "Mike", dojo = seattle)


# x = Dojo.objects.first().ninjas
# print x

def delete_ninjas():
    all_ninjas = Ninja.objects.all()
    for ninja in all_ninjas:
        ninja.delete()

def delete_dojos():
    all_dojos = Dojo.objects.all()
    for dojo in all_dojos:
        dojo.delete()

def print_ninjas():
    all_ninjas=Ninja.objects.all()
    for ninja in all_ninjas:
        print ninja.first_name,"\t",ninja.last_name,"\t",ninja.dojo.name

def print_dojos():
    all_dojos=Dojo.objects.all()
    for dojo in all_dojos:
        print dojo.id, "\t", dojo.name,"\t", dojo.city,"\t", dojo.state

def create_dojos():
    Dojo.objects.create(name="Coding Dojo Silicon Valley", city="Mountain View", state = "CA")
    Dojo.objects.create(name="Coding Dojo Seattle", city="Seattle", state = "WA")
    Dojo.objects.create(name="Coding Dojo New York", city="New York", state = "NY")
    Dojo.objects.create(name="Coding Dojo Chicago", city="Chicago", state = "IL")

def create_ninjas(city):    

    dojo=Dojo.objects.filter(city = city).first()
    Ninja.objects.create(first_name="Sam", last_name="Dunno", dojo =dojo)
    Ninja.objects.create(first_name="John", last_name="P", dojo =dojo)
    Ninja.objects.create(first_name="Bald", last_name="Mike", dojo =dojo)
    Ninja.objects.create(first_name="Prin.", last_name="Alyssa", dojo =dojo)



delete_ninjas()
delete_dojos()

print '+=  1  '+'+='*30
create_dojos()
print_dojos()
#print_ninjas

print '+=  2  '+'+='*30
delete_dojos()
print_dojos()

print '+=  3  '+'+='*30
create_dojos()
print_dojos()

print '+=  4  '+'+='*30
first_city = Dojo.objects.first().city
print first_city
create_ninjas(first_city)
print_ninjas()

print '+=  5  '+'+='*30
second_city = Dojo.objects.all()[1].city
print second_city
create_ninjas(second_city)
print_ninjas()

print '+=  6  '+'+='*30
third_city = Dojo.objects.all()[2].city
print third_city
create_ninjas(third_city)
print_ninjas()

print '+=  7  '+'+='*30
first_ninjas=Ninja.objects.filter(dojo__city=first_city)
for ninja in first_ninjas:
    print ninja.first_name,"\t",ninja.last_name,"\t",ninja.dojo.name

print '+=  8 '+'+='*30
last_city=Dojo.objects.order_by('created_at').reverse().first().city
print last_city
print first_city
last_ninjas=Ninja.objects.filter(dojo__city=last_city)
for ninja in last_ninjas:
    print ninja.first_name,"\t",ninja.last_name,"\t",ninja.dojo.name

