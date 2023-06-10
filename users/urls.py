from .views import login_view, home_view, logout_view,register_view, post_detail_view, react_post_view
from django.urls import path 

urlpatterns = [
    path("login/", login_view, name="login_view"),
    path("home/", home_view, name="home_view"),
    path("post/<id>/", post_detail_view, name="post_detail_view"),
    path("react-post/<id>/", react_post_view, name="react_post_view"),
    path("logout/", logout_view, name="logout_view"),
    path("register/", register_view, name="register_view")
]


