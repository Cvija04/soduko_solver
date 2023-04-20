from django.urls import path
from .views import SolveBoardView, GenerateBoardView

urlpatterns = [
    path('solver/', SolveBoardView.as_view(), name='solver'),
    path('random/', GenerateBoardView.as_view(), name='random')
]