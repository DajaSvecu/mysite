from django.urls import path

# Slouzi jako krizovatka pri pozadavcich (requests) od uzivatele
from . import views

app_name = 'todo'
urlpatterns = [
    # /todo/
    path('', views.HlavniView.as_view(), name='index'),
    # /todo/3
    #path('<int:user_id>/', views.detail, name='detail') #user_id musi by stejne jako ve view
    path('<int:pk>/', views.TodoView.as_view(), name= 'detail'),
    # /todo/3/finished
    path('<int:pk>/finished', views.FinishedView.as_view(), name='finished')
]
