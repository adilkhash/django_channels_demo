from django.conf.urls import url

from .views import home, MailMeView

urlpatterns = [
    url(r'^index$', home),
    url(r'^email$', MailMeView.as_view(), name='mailme'),
]
