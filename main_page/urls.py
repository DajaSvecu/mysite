from django.urls import path

# Slouzi jako krizovatka pri pozadavcich (requests) od uzivatele
from . import views

app_name = 'main_page'
urlpatterns = [
    # /
    path('', views.MainView.as_view(), name='main_page')
]
