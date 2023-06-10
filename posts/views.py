from django.shortcuts import render, redirect
from posts.models import UserPostsModel
from django.http import HttpResponse

# Create your views here.
def create_post(request):
    try:
        if not request.user.is_authenticated:
            return redirect("login_view")
        if request.method == "POST":
            print(request.POST)
            title = request.POST["title"]
            description = request.POST["description"]
            media = request.POST["img"]
            user = request.user
            UserPostsModel.objects.create(
                title = title,
                description = description,
                media = media,
                user = user 
            )

        return render(request, "posts/create_post.html")
    except Exception as e:
        return HttpResponse(f"something went wrong, {str(e)}")