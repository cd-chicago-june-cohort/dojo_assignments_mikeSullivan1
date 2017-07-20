
#from apps.books_authors.models import *

def create_books():
    titles = ["C sharp", "Java", "Python", "PHP", "Ruby"]
    for title in titles:
        Book.objects.create(name=title, desc="This is a book about %s" % title)

def print_books():
    books = Book.objects.all()
    for book in books:
        if book.authors:
            for author in book.authors.all():
                print author.first_name, author.last_name, '&',
            #print book.name,book.authors.first_name, authors.last_name
        else:
            print book.name
        
def print_authors():
    authors = Author.objects.all()
    for author in authors:
        print author.first_name,author.last_name, author.email, author.notes

def delete_books():
    for book in Book.objects.all():
        book.delete()

def delete_authors():
    for author in Author.objects.all():
        author.delete()


def create_authors():
    Author.objects.create(first_name ="Mike", last_name="Sullivan", email="sullyut@gmail.com")
    Author.objects.create(first_name ="Speros", last_name="Sullivan", email="jay@gmail.com")
    Author.objects.create(first_name ="John", last_name="Sullivan", email="mom@gmail.com")
    Author.objects.create(first_name ="Jadee", last_name="Sullivan", email="sis@gmail.com")
    Author.objects.create(first_name ="Jay", last_name="Sullivan", email="peah@gmail.com")



delete_authors()
#2
create_authors()
delete_books()
#1
create_books()
# print "#" * 100
print_books()

# #4
# print "#" * 100
# b = Book.objects.all()[4]
# b.name = "C#"
# b.save()
# print_books()

# #5
# print "#" * 100
print_authors()
# print "X" * 100
# a=Author.objects.all()[4]
# a.first_name="Ketul"
# a.save()
# print_authors()

print "#" * 100
# print "#" * 100
print_books()
print "#" * 100
# # pr

# # 

first_author = Author.objects.get(first_name='Mike')
first_author.save()

first_book = Book.objects.get(name='C sharp')
first_book.save()

second_book = Book.objects.get(name='Java')
second_book.save()

first_author.books.add(first_book, second_book)
first_author.save()

author_books = Book.objects.filter(authors__first_name='Mike')
for book in author_books:
    print book.name

print_books()
    