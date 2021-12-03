from django.urls import path
from users.api.views import UserAPIView

urlpatterns = [
    path("user/",UserAPIView.as_view(), name ="current-user")
]