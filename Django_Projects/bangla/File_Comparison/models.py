from django.db import models



class Document(models.Model):
    first_description=models.CharField(max_length=255,blank=True)
    second_description=models.CharField(max_length=255,blank=True)

    first_document=models.FileField(upload_to='documents/django/')
    second_document=models.FileField(upload_to='documents/django/')

    upload_at=models.DateTimeField(auto_now_add=True)

