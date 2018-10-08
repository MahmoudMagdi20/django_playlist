from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Article

# Create your views here.
def article_list(request):
    template = loader.get_template('articles/article_list.html')
    articles = Article.objects.all().order_by('-date')
    return HttpResponse(template.render({'articles':articles}), request)

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})
