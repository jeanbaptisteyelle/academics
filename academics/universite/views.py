from django.shortcuts import render, get_object_or_404
from . import models
from website import models as website_models

# Create your views here.
def admission(request):
    cat = models.Caracteristique.objects.filter(status=True)
    reseaux = website_models.Reseau_social.objects.filter(status=True)
    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')
    admision =  models.Admisssion.objects.filter(status=True).latest('date_update')
    datas = {
        "siteinfo":siteinfo,
        "reseaux":reseaux,
        "cat":cat,
        "admision":admision,




        "admission":"active"
    }
    return render(request, 'pages/admission.html', datas)

def courses(request):
    cat = models.Caracteristique.objects.filter(status=True)
    reseaux = website_models.Reseau_social.objects.filter(status=True)
    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')
    cour = models.Cour.objects.filter(status=True)
    domaine = models.Domaine.objects.filter(status=True)
    datas = {
        "siteinfo":siteinfo,
        "reseaux":reseaux,
        "cat":cat,
        "cour":cour,
        "domaine":domaine,


        "cours":"active"
    }
    return render(request, 'pages/courses.html', datas)

def course_single(request):
    cat = models.Caracteristique.objects.filter(status=True)
    reseaux = website_models.Reseau_social.objects.filter(status=True)
    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')
    cour = models.Cour.objects.filter(status=True).latest('date_update')
    domaine = models.Domaine.objects.filter(status=True).latest('date_update')
    

    datas = {
        "siteinfo":siteinfo,
        "reseaux":reseaux,
         "cour":cour,
         "domaine":domaine,
         "cat":cat,
    }
    return render(request, 'pages/course-single.html', datas)

def news_single(request,slug):
    blog = models.Blog.objects.get(slug=slug)
    reseaux = website_models.Reseau_social.objects.filter(status=True)
    siteinfo = website_models.Siteinfo.objects.filter(status=True).latest('date_update')
    cat = models.Caracteristique.objects.filter(status=True)
    single_new = get_object_or_404(models.Blog, slug=slug)

    
    datas = {
        "blog":blog,
       "siteinfo":siteinfo,
        "reseaux":reseaux,
        "cat":cat,
        "single_new":single_new,
        
    }
    return render(request, 'pages/news-single.html', datas)