from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from main.encriptor import connect_db, dict_creator


def signup(request):

    if request.method == "POST":
        user = User()
        user.first_name = request.POST.get("First_Name")
        user.last_name = request.POST.get("Last_Name")
        user.username = request.POST.get("Username")

        passs = request.POST.get("Password")
        user.set_password(passs)

        user.save()

        db = connect_db()
        crsr = db.cursor()

        dictt = str(dict_creator())

        c = "INSERT INTO user_dicts (username, dictt)" + "\n" f'VALUES ("{user.username}", "{dictt}")'

        print(c)
        
        crsr.execute(c)
        
        db.commit()
        db.close()


        return redirect("login")
        

    return render(request, "useraccount/signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        password = request.POST.get("Password")

        user = auth.authenticate(username = username, password = password)
        if user is None:
            return redirect("login")
        else:
            auth.login(request, user)
            return redirect("/")
    else:
        return render(request, "useraccount/login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")
