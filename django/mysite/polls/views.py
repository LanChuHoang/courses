from db.db import db, te
from django.http import HttpResponse

# print(te)
print(db)
print(te)


def index(request):
    return HttpResponse("Hello you're at the polls index")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
