from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        user = {
            'name': 'One',
            'mail': "one@one.ru"
        }

        return render(request, 'article_view.html', {
            'title': request.POST.get("title"),
            'content': request.POST.get("content"),
            'author': request.POST.get("author"),
            'user': user
        })
