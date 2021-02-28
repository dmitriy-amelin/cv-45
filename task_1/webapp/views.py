from django.shortcuts import render

from webapp.models import Article


def index_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }

    return render(request, 'index.html', context)


def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.POST.get("author")

        article = Article.objects.create(
            title=title,
            content=content,
            author=author
        )

        return render(request, 'home.html')
