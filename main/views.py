from django.shortcuts import render
from ast import literal_eval
from .encriptor import connect_db, decript, encript

def encript_view(request):
    def user_logged_in(request):
        if request.user.is_authenticated:
            return True
        return False

    if request.method == "POST":

        db = connect_db()
        crsr = db.cursor()

        if user_logged_in(request) :
            c = "SELECT dictt FROM user_dicts" + "\n" + f"WHERE username = '{request.user.username}'"
        else:
            c = "SELECT dictt FROM user_dicts" + "\n" + "WHERE username = 'hrk'"

        crsr.execute(c)
        dictt = literal_eval(crsr.fetchall()[0][0])
        db.close()

        out = encript(request.POST.get("inp"), dictt)

        return render (request, 'main/index.html', {"out":out})

    out = "Enter the text here"

    return render (request, 'main/index.html', {"out":out})

def decript_view(request):
    def user_logged_in(request):
        if request.user.is_authenticated:
            return True
        return False

    if request.method == "POST":
        db = connect_db()
        crsr = db.cursor()

        if user_logged_in(request) :
            c = "SELECT dictt FROM user_dicts" + "\n" + f"WHERE username = '{request.user.username}'"
        else:
            c = "SELECT dictt FROM user_dicts" + "\n" + "WHERE username = 'hrk'"

        crsr.execute(c)
        dictt = literal_eval(crsr.fetchall()[0][0])
        db.close()

        out = decript(request.POST.get("inp"), dictt)

        return render (request, 'main/index.html', {"out":out})

    out = "Enter the text here"

    return render (request, 'main/index.html', {"out":out})

