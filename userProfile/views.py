from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def feed(request):
    return render(request, 'userProfile/feed.html')


@login_required
def profile(self):
    return render(self, 'userProfile/user_profile.html')
