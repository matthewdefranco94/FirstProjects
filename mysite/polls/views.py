from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #for each question, give us it's text and join it by commas
    output = ', '.join([q.question_text for q in latest_question_list])
    #then return it as our output
    return HttpResponse(output)

def detail(request , question_id):
    #question number(%s) with the qustion_id
    return HttpResponse("You're looking at question %s." % question_id)

def results(request , question_id):
    response = "You're looking at the results of qustion %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
