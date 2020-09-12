from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Question, Choice, Comment
from .forms import QuestionForm
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls_3/index.html'
    context_object_name = 'list_of_question'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls_3/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls_3/results.html'

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls_3/detail.html', {
            'question': question,
            'error_message': "You didn't select choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

def post_new(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.pub_date = timezone.now()
            question.save()
            return redirect('detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'polls_3/edit.html', {'form': form})

def edit(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.pub_date = timezone.now()
            question.save()
            return redirect('detail', pk=question.pk)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'polls_3/edit.html', {'form': form})