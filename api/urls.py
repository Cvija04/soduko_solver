from django.urls import path
from .views import SolveBoardView, GenerateBoardView

urlpatterns = [
    path('solver/', SolveBoardView.as_view(), name='solver'),
    path('generate/', GenerateBoardView.as_view(), name='generate_board')
]
