from django.shortcuts import render,redirect
from . import models
from universite import models as universite_models
 
from django.contrib.auth import authenticate,login,logout
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def newletter(request):
       if request.method=='POST':
        email = request.POST.get('email')
        try:
            validate_email(email)
            if  email is not None :
                newletter = models.Newletter(
                    email = email,

                )
                newletter.save()
                messages.success(request,"vos informations ont été enregistré")
            else:
                messages.error(request,"email incorect")
             
        except:
            messages.error(request, "veuillez entrer un email correct")
        return redirect(request.META.get('HTTP_REFERER', '/'))






def index(request):

    siteinfo = models.Siteinfo.objects.filter(status=True).latest('date_update')
    slide = models.Slice.objects.filter(status=True)
    reseaux = models.Reseau_social.objects.filter(status=True)
    caracteristique = universite_models.Caracteristique.objects.filter(status=True)
    cours = universite_models.Cour.objects.filter(status=True)
    domaine = universite_models.Domaine.objects.filter(status=True)
    
    temoignage = models.Temoignage.objects.filter(status=True)[:3]
    cat = universite_models.Caracteristique.objects.filter(status=True)
    blog = universite_models.Blog.objects.filter(status=True)
    video = universite_models.Video.objects.filter(status=True)
    datas = {
        "siteinfo":siteinfo,
        "slide":slide,
        "reseaux":reseaux,
        "caracteristique":caracteristique,
        "cours":cours,
        "domaine":domaine,
        "about":about,
        "temoignage":temoignage,
        "cat":cat,
        "blog":blog,
        "video":video,




        "home":"active"
    }
    return render(request, 'pages/index.html', datas)

def about(request):
    reseaux = models.Reseau_social.objects.filter(status=True)
    siteinfo = models.Siteinfo.objects.filter(status=True).latest('date_update')
    aboutt = models.Aboutt.objects.filter(status=True)
    caracteristique = universite_models.Caracteristique.objects.filter(status=True)
    cat = universite_models.Caracteristique.objects.filter(status=True)  
    teacher = models.Enseignant.objects.filter(status=True) 
    datas = {
        "siteinfo":siteinfo,
        "reseaux":reseaux,
        "aboutt":aboutt,
        "caracteristique":caracteristique,
        "cat":cat,
        "teacher":teacher,
       






        "about":"active"

    }

    return render(request, 'pages/about.html', datas)



def contact(request):
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        message = request.POST.get('message')
        print(firstname,lastname,email,telephone,message)
        try:
            validate_email(email)
            if firstname is not None and lastname is not None and email is not None and telephone is not None and message is not None:
                contact = models.Contact(
                    email = email,
                    firstname = firstname,
                    lastname = lastname,
                    telephone = telephone,
                    message = message,

                )
                contact.save()
                messages.success(request,"vos informations ont été enregistré")
            else:
                print("1 2 3")
                messages.error(request,"veuillez entrer des informations correctes")
             
        except Exception as e:
            print(e)
            messages.error(request, "veuillez verifier les informations entrées")
        return redirect(request.META.get('HTTP_REFERER', '/'))







    cat = universite_models.Caracteristique.objects.filter(status=True)  
    reseaux = models.Reseau_social.objects.filter(status=True)
    siteinfo = models.Siteinfo.objects.filter(status=True).latest('date_update')
    datas = {
        "reseaux":reseaux,
        "siteinfo":siteinfo,
        "cat":cat,



        "contact":"active"
    }
    return render(request, 'pages/contact.html', datas)



def login_view(request):
    message=""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)

            return redirect('index')
        else:
            print("login échoué")
            message = "Merci de vérifiez vos informations"


    reseaux = models.Reseau_social.objects.filter(status=True)
    siteinfo = models.Siteinfo.objects.filter(status=True).latest('date_update')
    datas = {
        "reseaux":reseaux,
        "siteinfo":siteinfo,
    }
    return render(request, 'pages/login.html', datas)

def register(request):
    success = False
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        print(username,email,password,confirm)
        if password != confirm:
            success = True
            message = "mot de passe incorrect"
            print("mot de passe incorrect")
        else:
            message = "correct"
            print("success")
            try:
                print("1")
                validate_email(email)
                isemail = True
                if isemail and not email.isspace() and username is not None and password is not None and confirm is not None:
                    try:
                        print("2")
                        try:
                            exist_user = User.objects.get(username=username)
                        except :
                            exist_user = User.objects.get(email=email)

                        message = "un utilisateur avec le même username est déjà connecté"
                        success = True 
                    except Exception as e :
                        print("3", e)
                        user = User(
                            username=username,
                            email=email,
                            password=password,
                        )
                        user.save() 
                        user.password = password
                        user.set_password(user.password)
                        user.save()

                        try:
                            us = authenticate(username=username, password=password)
                            if us.is_active:
                                login(request,us)
                                return redirect('login')
                        except Exception as e:
                            print("4", e)


            except Exception as e:
                success = True 
                print("5", e)
                message = "l'inscription a échoué"
                print("inscription echoué")

    reseaux = models.Reseau_social.objects.filter(status=True)
    siteinfo = models.Siteinfo.objects.filter(status=True).latest('date_update')

    datas = {

        "success":success,
        "message":message,
        "reseaux":reseaux,
        "siteinfo":siteinfo,
        
    }
    return render(request, 'pages/register.html', datas)

