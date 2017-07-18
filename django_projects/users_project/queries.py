from apps.users.models import *

# b = User.objects.get(id=3)
# b.last_name = "Pelican"
# b.save()

#User.objects.get(id=4).delete()
print b.first_name, b.last_name, b.email


all_users = User.objects.all()
for user in all_users:
     print user.first_name, user.last_name, user.email


