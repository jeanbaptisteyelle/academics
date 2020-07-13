from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Siteinfo(models.Model):
    slogan = models.CharField(max_length=255)
    titre_about = models.CharField(max_length=255)
    about_description = models.TextField(null='True')
    single_cours_titre = models.CharField(max_length=255,null='True')
    single_news_titre = models.CharField(max_length=255,null='True')
    single_cours_description = models.TextField(null='True')
    about_image = models.ImageField(upload_to='images/aboutsite')
    description = models.TextField()
    description_cours = models.TextField(null='True')
    description_footer = models.TextField()
    admission_description = models.TextField()
    telephone = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='images/logo')
    logo_footer = models.ImageField(upload_to='images/logofooter')
    email = models.EmailField()
    caracteristique_bg = models.ImageField(upload_to='images/caracteristique')
    login_description = models.TextField(null='True')
    register_description = models.TextField(null='True')
    contact_description = models.TextField(null='True')

    bg_autre = models.ImageField(upload_to='images/autre')
    
    newletter_bg = models.ImageField(upload_to='images/newletter') 
    newletter_title = models.CharField(max_length=255) 
    newletter_description = models.TextField()

    copyrights = models.CharField(max_length=255) 

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = ("Siteinfo")
        verbose_name_plural = ("Siteinfos")

    def __str__(self):
        return self.newletter_title 

class Newletter(models.Model):
    email = models.EmailField(max_length=255)

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Newletter")
        verbose_name_plural = ("Newletters")

    def __str__(self):
        return str(self.email)

class Aboutt(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    description2 = models.TextField()
    image = models.ImageField(upload_to='image/aboutt')
    
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Aboutt")
        verbose_name_plural = ("Aboutts")

    def __str__(self):
        return self.titre

class Contact(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField( max_length=255)
    telephone = models.CharField(max_length=255)
    message = models.TextField()

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.firstname

class Slice(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/slice')
    
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Slice")
        verbose_name_plural = ("Slices")

    def __str__(self):
        return self.titre

class Caracteristique(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Caracteristique")
        verbose_name_plural = ("Caracteristiques")

    def __str__(self):
        return self.nom

class Enseignant(models.Model):
    nom = models.CharField(max_length=255)
    matiere = models.CharField(max_length=255)
    biographie = models.TextField()
    photo = models.ImageField(upload_to='images/enseignant')

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Enseignant")
        verbose_name_plural = ("Enseignants")

    def __str__(self):
        return self.nom

class Reseau_social(models.Model):
    ICONE = [
        ('icon-facebook', 'facebook'),
        ('icon-twitter', 'twitter'),
        ('icon-linkedin', 'linkedin'),
    ]
    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icone = models.CharField(choices = ICONE, max_length=255)

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Reseau_social")
        verbose_name_plural = ("Reseau_sociaux")

    def __str__(self):
        return self.nom

class Temoignage(models.Model):
    nom = models.CharField(max_length=255)
    fonction = models.CharField(max_length=255)
    Temoignage = models.TextField()
    photo = models.ImageField( upload_to='images/temoignage')
    
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Temoignage")
        verbose_name_plural = ("Temoignages")

    def __str__(self):
        return self.nom











   