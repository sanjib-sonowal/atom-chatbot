from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'chatbot/index.html')


def chatbot_help(request):
    return render(request, 'chatbot/help.html')


def developers(request):
    return render(request, 'chatbot/developers.html')