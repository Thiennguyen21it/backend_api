from django.urls import path
from .views import SignUpAPIView,LogoutAPIView , LoginAPIView

urlpatterns = [
    path('  /', SignUpAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]




# from django.urls import path
# from .views import LoginView, LogoutView, PostView
# # urlpatterns = [
# #     path('login/', LoginAPIView.as_view(), name='login'),
# # ]

# urlpatterns = [
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('post/', PostView.as_view(), name='post'),
# ]