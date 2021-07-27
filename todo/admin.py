from django.contrib import admin

# Register your models here.
# Umoznuje manipulovat s modely/tabulky (User, Todoitems) v admin prostredi
from .models import User

admin.site.register(User)