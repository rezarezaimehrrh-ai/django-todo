from django.shortcuts import redirect, render, get_object_or_404

# from django.views.decorators.cache import never_cache
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

#   sign up or log in   #


def sign_log(request):
    if request.method == "POST":
        signup_button = request.POST.get("signup_button")
        login_button = request.POST.get("login_button")

        if signup_button:
            return redirect("sign_up")
        elif login_button:
            return redirect("login")

    return render(request, "todo_app/sign_log.html")

    #   sign up   #


def sign_up(request):

    if request.method == "POST":

        suser_name = request.POST.get("signup_username")
        spass_word = request.POST.get("signup_password")
        signup_enter = request.POST.get("signup_enter")
        con_password = request.POST.get("con_password")
        login_button = request.POST.get("login_button")
        user_exists = User.objects.filter(username=suser_name).exists()

        if user_exists:

            return render(
                request, "todo_app/sign_up.html", {"user_exists": user_exists}
            )

        elif suser_name and spass_word == con_password and signup_enter:

            user = User.objects.create_user(username=suser_name, password=spass_word)

            messages.success(request, "Account created successfully.")
            login(request, user)
            return redirect("add_page")

        elif login_button:

            return redirect("login")

    return render(request, "todo_app/sign_up.html")

    #   log in   #


def log_in(request):

    if request.method == "POST":

        user_name = request.POST.get("user_name")
        pass_word = request.POST.get("pass_word")
        enter = request.POST.get("login_enter")
        signup_button = request.POST.get("signup_button")

        user = authenticate(request, username=user_name, password=pass_word)

        print(user)
        print(enter)

        if user and enter:

            login(request, user)

            return redirect("add_page")

        elif not user and enter:
            messages.error(request, "Invalid username or password")
            return redirect("login")

        elif signup_button:
            return redirect("sign_up")

    return render(request, "todo_app/login.html")
