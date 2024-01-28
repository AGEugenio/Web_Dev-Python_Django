from django.urls import path
# from challenge folder
from . import views
# list for all url patterns we want
urlpatterns = [
    # when the url is /challenges/jan, execute the views function
    # path("jan", views.january),
    
    #path for /challenges/
    path("",views.index),

    # if you don't care the concrete value;create a dynamic path
    # month is the identifier for the given value
    path("<int:month>", views.monthly_challenge_by_number),
    # name django keyword is added and it can be used to cosntruct path's
    path("<str:month>", views.monthly_challenge, name="month-challenge")



]
