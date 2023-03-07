from django.db import models

'''
# Create your models here.
class SecurityQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    class Meta:
        app_label = 'password_app'
    

class GeneratedPassword(models.Model):
    password = models.CharField(max_length=255)
'''

from django.db import models

class SecurityQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class GeneratedPassword(models.Model):
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.password

     