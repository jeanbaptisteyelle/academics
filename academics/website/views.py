from django.shortcuts import render,redirect
from . import models
from universite import models as universite_models

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
        email = request.POST.get('email')
        try:
            validate_email(email)
            if  email is not None :
                newletter = models.Contact(
                    email = email,

                )
                newletter.save()
                messages.success(request,"vos informations ont été enregistré")
            else:
                messages.error(request,"email incorect")
             
        except:
            messages.error(request, "veuillez entrer un email correct")
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



def login(request):
    reseaux = models.Reseau_social.objects.filter(status=True)
    siteinfo = models.Siteinfo.objects.filter(status=True).latest('date_update')
    datas = {
        "reseaux":reseaux,
        "siteinfo":siteinfo,
    }
    return render(request, 'pages/login.html', datas)

def register(request):
    reseaux = models.Reseau_social.objects.filter(status=True)
    siteinfo = models.Siteinfo.objects.filter(status=True).latest('date_update')

    datas = {
        "reseaux":reseaux,
        "siteinfo":siteinfo,
        
    }
    return render(request, 'pages/register.html', datas)

