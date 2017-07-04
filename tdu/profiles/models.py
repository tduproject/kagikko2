from django.db import models
from django.utils import timezone
from encrypted_fields import EncryptedTextField ,EncryptedEmailField,EncryptedCharField,EncryptedIntegerField
class UserProfile(models.Model):

    name = EncryptedCharField(max_length = 254)
    email = models.EmailField(max_length= 254 , default = 'example@example.com')
    grade = models.CharField(max_length = 254)
    major = EncryptedCharField(max_length = 254)
    text = EncryptedTextField()
    # name = models.CharField(max_length = 20)
    # email = models.EmailField(max_length = 254,default='example@me.com')
    # grade = models.CharField(max_length = 5)
    # major = models.CharField(max_length = 5)
    # text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
