from django.db import models
import re

class UserManager(models.Manager):

    def basic_validator(self, postData):
        errors={}
        if len(postData['fname'])<2 or not postData['fname'].isalpha():
            errors["fname"] = " first name must be greater than 2 charecters"

        if  len(postData['lname'])<2 or not postData['fname'].isalpha():
            errors["lname"] = " last name must be greater than 2 charecters"

        if len(postData['password'])<8:
            errors["password"]= "password must be greater than 8"

        if postData['password'] !=postData['pw']:
            errors['matches']="password not matches"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):               
            errors['email'] = "Invalid email address"

        return errors









# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.TextField()
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()


class Message(models.Model):
        user = models.ForeignKey(User ,related_name="messages",on_delete=models.CASCADE)
        message=models.TextField()
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
        message=models.ForeignKey(Message,related_name="comments",on_delete=models.CASCADE)
        user=models.ForeignKey(User,related_name="comments",on_delete=models.CASCADE)
        comment=models.TextField()
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)


