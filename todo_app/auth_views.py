from django.shortcuts import redirect , render , get_object_or_404
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .models import User


                #   sign up or log in   #
@never_cache
@login_required

def sign_log(request):
    if request.method=="POST":
        signup_button= request.POST.get("signup_button")
        login_button= request.POST.get("login_button")
    
        if signup_button:
            return redirect("sign_up")
        elif login_button:
            return redirect("login")
        
    return render(request , "todo_app/sign_log.html")


                #   sign up   #

@never_cache
@login_required

def sign_up(request):

    if request.method=="POST":


            suser_name= request.POST.get("signup_username")
            spass_word= request.POST.get("signup_password")
            signup_enter= request.POST.get("signup_enter")
            con_password= request.POST.get("con_password")
            login_button= request.POST.get("login_button")
            


            if suser_name and spass_word==con_password and signup_enter:

                

                User.objects.create(
                    username = suser_name , password = spass_word
                    )


                return redirect("sign_log")
            
            elif login_button:

                return redirect("login")
    
    return render(request , 'todo_app/sign_up.html')





                #   log in   #
@never_cache
@login_required

def log_in(request):

    if request.method=="POST":

        user_name = request.POST.get("user_name")
        pass_word = request.POST.get("pass_word")
        enter= request.POST.get("login_enter")
        signup_button= request.POST.get("signup_button")
       

        user = User.objects.filter(username = user_name, password = pass_word).first()

        
        
        if user and enter:

            request.session ["user_id"] = user.id
            request.session.get("user_id")
        
            return redirect("add_page")
        
        elif signup_button:
            return redirect("sign_up")
        
    return render(request , 'todo_app/login.html')



