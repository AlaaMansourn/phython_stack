from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title'])<2 or not postData['title'].isalpha():
            errors["title"]="The title should be more than two charecters and has words"
        if len(postData['network'])<2 or not postData['network'].isalpha():
            errors["network"]="The network should be more than two charecters and has words"

        if len(postData['description'])<2 or not postData['description'].isalpha():
            errors["description"]="The description should be more than two charecters and has words"
        return errors

class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    release_date=models.DateField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = ShowManager()
        
# Create your models here.
