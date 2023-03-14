from django.shortcuts import render
from main.models import Main


def main_page(request):
    posts = Main.objects.all()
    return render(request,
                  'main/main_page.html',
                  {'posts': posts})
