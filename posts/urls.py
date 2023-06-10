from django.urls import path 
from .views import create_post, update_post, delete_post


urlpatterns = [
    path("create-post/", create_post, name="create_post"),
    path("update-post/<id>/", update_post, name="update_post"),
    path("delete-post/<id>/",delete_post, name="delete_post"),
]
