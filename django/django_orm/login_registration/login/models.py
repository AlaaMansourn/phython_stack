from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


    def register(username,passwd):
        Users.objects.create(username=username,password=passwd)
    

    def check_user(name,passwd):
        user=Users.objects.filter(username=name)
        if user==None:
            return False
            
        if user.password==passwd:
            return True

        return False