from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)


    def __str__(self):
        return self.username

class Messaging(models.Model):

    message_id = models.IntegerField()
    sender = models.ForeignKey('User',on_delete=models.CASCADE, related_name='sender')
    recevier = models.ForeignKey('User',on_delete=models.CASCADE, related_name='recevier')
    content = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
    readable = models.CharField(max_length=10)



