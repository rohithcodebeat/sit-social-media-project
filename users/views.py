from django.shortcuts import render , redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from posts.models import UserPostsModel

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home_view")
        else:
            return render(request,
                           "users/login.html",
                             context={"error_message" : "Invalid Username or Password"})    
    else:
        return render(request, "users/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password != confirm_password:
            context = {
                "error" : True,
                "error_message" : "Password does not match"
            }
            return render(request, "users/register.html", context)
        
        user = get_user_model().objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        return redirect("login_view")
    
    return render(request, "users/register.html")

def home_view(request):
    if request.user.is_authenticated:
        user_posts_query = UserPostsModel.objects.filter(is_active=True)
        likes_dict = {}
        for query in user_posts_query:
            likes_dict[query.id] = query.likes.all().count()
        context = {
            "username" : request.user.username,
            "is_user_login" : True,
            "likes_dict" : likes_dict,
            "user_posts_query" : user_posts_query
        }
    else:
        
        context = {
            "username" : "UnAuthorized User",
            "is_user_login" : False            

        }
    return render(request, "users/home.html", context)


def post_detail_view(request, id):
    if request.user.is_authenticated:
        user_posts_query = UserPostsModel.objects.filter(is_active=True).get(id=id)
        context = {
            "username" : request.user.username,
            "is_user_login" : True,
            "is_liked" : user_posts_query.likes.all().filter(username=request.user.username).exists(),
            "likes_count" : user_posts_query.likes.all().count(),
            "obj" : user_posts_query
        }
    else:
        
        context = {
            "username" : "UnAuthorized User",
            "is_user_login" : False            

        }
    return render(request, "users/detail_post.html", context)


def logout_view(request):
    logout(request)
    return redirect("login_view")


def react_post_view(request, id):
    if not request.user.is_authenticated:
        return redirect("login")

    post_query = UserPostsModel.objects.get(id=id)
    if post_query.likes.all().filter(username=request.user.username).exists():
        post_query.likes.remove(request.user)
    else:
        post_query.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))




