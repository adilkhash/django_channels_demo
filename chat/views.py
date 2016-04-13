from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from channels.channel import Channel

from .forms import MailMeForm


def home(request):
    return render(request, 'chat.html')


class MailMeView(View):
    def get(self, request):
        return render(request, 'mailme.html', {'form': MailMeForm()})

    def post(self, request):
        form = MailMeForm(request.POST)

        if form.is_valid():
            Channel('send_email').send({'payload': form.cleaned_data})
            return HttpResponse('Good job!')
        else:
            return render(request, 'mailme.html', {'form': form})
