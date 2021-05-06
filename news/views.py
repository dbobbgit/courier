from django.shortcuts import render

# Create your views here.

from news.models import Article, Author

def index(request):
    posts = Article.objects.all()
    return render(request, 'index.html', {'posts': posts})

def article_detail(request, post_id: int):
    post = Article.objects.get(id=post_id)
    return render(request, 'article_detail.html', {'post': post})


def author_detail(request, author_id: int):
    my_author = Author.objects.get(id=author_id)
    author_posts = Article.objects.filter(author=my_author)
    return render(request, 'author_detail.html', 
    {'author': my_author, 'posts': author_posts})