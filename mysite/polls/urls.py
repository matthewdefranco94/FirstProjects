from django.urls import path

from . import views

#goes to empty path
#then goes into views file and uses index function
#we can use this index so we can refer to it later
urlpatterns = [
    #ex: /polls/ goes to the empty pattern after pulls, and run the function 'index'
    path('' , views.index , name = 'index'),
    #ex /polls/5/ #dynamically matches patterns with the int:""
    path('<int:question_id>/', views.detail, name='detail'),
    #ex: /polls/5/results
    path('<int:question_id>/results/', views.results, name='results'),
    #ex: /polls/5/vote
    path('<int:question_id>/vote/', views.vote , name='vote')
]