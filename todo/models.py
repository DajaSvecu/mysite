from django.db import models

# Create your models here.
# Vytvari tabulky (TABLE) v databazi
# Automaticky vytvari primary_key
class User(models.Model):
    user_name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    def __str__(self):
        # slouzi jako reprezentace objektu v TABLE
        return self.user_name
    
class Todoitems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    def __str__(self):
        return self.item
