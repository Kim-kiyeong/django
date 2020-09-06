from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from .models import Question, Choice
from .forms import QuestionForm

def base(request):
    return render(request, 'polls_2/base.html')

class IndexView(generic.ListView):
    template_name = 'polls_2/index.html'
    context_object_name = 'list_of_latest_question'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    template_name = 'polls_2/detail.html'
    model = Question

class ResultsView(generic.DetailView):
    template_name = 'polls_2/results.html'
    model = Question

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls_2/detail.html', {
            'question': question,
            'error_message': "You didn't select Choice."
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

def new_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.pub_date = timezone.now()
            question.save()
            return redirect('detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'polls_2/new.html', {'form': form})