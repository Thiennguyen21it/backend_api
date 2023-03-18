from django.urls import path
from .views import SignUpAPIView,LogoutAPIView , LoginAPIView, ImageAPIView, PostVideoAPIView, CommentAPIView, UserList

urlpatterns = [
    path('users/', UserList.as_view(), name='users'),
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('postphoto/', ImageAPIView.as_view(), name='postphoto'),
    path('postvideo/', PostVideoAPIView.as_view(), name='postvideo'),
    path('comment/', CommentAPIView.as_view(), name='comment'),
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