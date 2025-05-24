from django.shortcuts import render

def index(request):
    return render(
        request,               # Так будет всегда
        'mainpage/main.html',  # Путь к шаблону
    )
