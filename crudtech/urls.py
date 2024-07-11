from django.urls import path
from .views import contain, only

urlpatterns = [
    path('myway/', contain),  #Idsiz umumiy ma'lumotni so'rovchi qism
    path('myway/<int:pk>', only) #ID bilan chaqirib oladigan qism
]