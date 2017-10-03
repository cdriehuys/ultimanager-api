"""
URL routing for account views.
"""

from django.conf.urls import url

from account import views


urlpatterns = [
    url(r'^register/$', views.RegistrationView.as_view(), name='register'),
]
