from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Message(models.Model):
    sender=models.ForeignKey(User,related_name='sent_messages',on_delete=models.CASCADE)
    receiver=models.ForeignKey(User, related_name='recieved_mesage', on_delete=models.CASCADE)
    message=models.TextField()
    seen=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)

    class Meta:
    	ordering=('date_created',)
    

    