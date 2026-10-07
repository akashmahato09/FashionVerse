from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_login(request):
    if request.method== 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        num_of_items = request.session.get("num_of_items", 0)
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("core:home")
        else:
            return redirect("accounts:user_login")
    return render(request, "accounts/user_login.html")



def user_register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")

        if password == password1:

            if User.objects.filter(username=username).exists():
                return render(request, "accounts/user_register.html", {
                    "error": "Username already exists."
                })

            if User.objects.filter(email=email).exists():
                return render(request, "accounts/user_register.html", {
                    "error": "Email already exists."
                })

            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            return redirect("accounts:user_login")

        else:

            return render(request, "accounts/user_register.html", {
                "error": "Passwords do not match."
            })

    return render(request, "accounts/user_register.html")


def logout_user(request):
    logout(request)              # Clears the user's session
    return redirect("core:home")