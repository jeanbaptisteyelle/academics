from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
from django.utils.text import slugify 
import time
zips = time.time()

# Create your models here.

class Caracteristique(models.Model):

    ICONES = [
        ('flaticon-school-material','School'),
        ('flaticon-mortarboard','Mortarboard'),
        ('flaticon-library','Library')

    ]

    nom = models.CharField(max_length=255)
    description = models.TextField()
    icone = models.CharField(choices = ICONES, max_length=255)

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Caracteristique")
        verbose_name_plural = ("Caracteristiques")

    def __str__(self):
        return self.nom


class Domaine(models.Model):
    content = HTMLField('Content', null='True')
    titre = models.CharField(max_length=255)
    prix = models.IntegerField()
    description = models.TextField()
    heure_debut = models.DateTimeField()
    heure_fin = models.DateTimeField()
    image = models.ImageField(upload_to='images/domaine')

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Domaine")
        verbose_name_plural =("Domaines")

    def __str__(self):
        return self.titre


class Cour(models.Model):
    nom = models.CharField(max_length=255)
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE, related_name='domaine_cour')

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Cour")
        verbose_name_plural = ("Cours")

    def __str__(self):
        return self.nom



class Admisssion(models.Model):
    content = HTMLField('Content')
    note = models.IntegerField()

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)


    class Meta:
        verbose_name = ("Admisssion")
        verbose_name_plural = ("Admisssions")

    def __str__(self):
        return str(self.note)


class Blog(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/blog')
    description = models.TextField(null='True')
 
    slug = models.SlugField(unique=True, null= True, blank=True)

    def save(self, *args, **kwargs):
        self.slug ='-'.join((slugify(self.titre),(slugify(zips))))
        super(Blog, self).save(*args, **kwargs)
    

    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Blog")
        verbose_name_plural = ("Blogs")

    def __str__(self):
        return self.titre

class Video(models.Model):
    lien = models.URLField()
    image = models.ImageField(upload_to='images/campus')
    titre = models.CharField(max_length=255, null=True)
    description = models.TextField()
    
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Video")
        verbose_name_plural = ("Videos")

    def __str__(self):
        return self.titre