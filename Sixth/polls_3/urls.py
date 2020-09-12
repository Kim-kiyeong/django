from django.urls import path
from . import views

urlpatterns = [
    path('polls_3/', views.IndexView.as_view(), name='index'),
    path('polls_3/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('polls_3/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('polls_3/<int:pk>/vote/', views.vote, name='vote'),
    path('polls_3/new/', views.post_new, name='post_new'),
    path('polls_3/<int:pk>/edit/', views.edit, name='edit'),
]