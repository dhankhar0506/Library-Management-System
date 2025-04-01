from django.db import models

class Record(models.Model):

    publication_date = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    Title = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    author = models.CharField(max_length=300)

    genre = models.CharField(max_length=200)


    def __str__(self):

        return self.first_name + "   " + self.last_name














