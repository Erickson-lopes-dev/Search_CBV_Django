from django.urls import path

from CBV_search.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home')
]
