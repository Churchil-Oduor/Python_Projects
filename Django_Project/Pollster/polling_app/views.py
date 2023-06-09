from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list' : latest_question_list}
    return render(request, "polls/index.html", context)

def details(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does not Exist")
    return render(request, "polls/details.html", {"question" : question})


def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request,  "polls/results.html", { "question" : question})


def vote(request,  question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice']);
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', 
                      {"question": question,
                       "error_message": "You did't select a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polling_app:results', args = (question.id,)))
    