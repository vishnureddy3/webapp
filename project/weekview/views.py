from django.shortcuts import render

# Create your views here.
from django.views.generic.dates import WeekArchiveView

from .models import Article
from django.views.generic import TemplateView

class ArticleWeekArchiveView(WeekArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    week_format = "%W"
    allow_future = True

def first(request):
    return render(request,"first.html")