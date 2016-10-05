from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question, Photo
from .api import login
# Create your views here.


def index(request):
    lql = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
            'latest_question_list': lql,
        })
    return HttpResponse(template.render(context))


def addPhotos(request):
    query = request.GET
    


def detail(request, question_id):
    return HttpResponse("You're looking at question %{}.".format(question_id))


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You look at vote of %s." % question_id)
