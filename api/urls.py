from django.urls import path
from .views import LoginView, LogoutView
# urlpatterns = [
#     path('login/', LoginAPIView.as_view(), name='login'),
# ]

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]