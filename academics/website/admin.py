from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Siteinfo)
class SiteinfoAdmin(admin.ModelAdmin):
    list_display = ('email','telephone','newletter_title','date_add','date_update','status','logo_view','caracteristique_bg_view','about_image_view','newletter_bg_view','logo_footer_view','bg_autre_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('telephone',)
    date_hierarchy = 'date_add'
    list_display_links = ['telephone']
    fieldsets = [
          ('Site_info', {'fields':['slogan','telephone', 'description','newletter_title','newletter_description','description_footer','copyrights','titre_about','about_description','about_image','logo','caracteristique_bg','newletter_bg','email','logo_footer','bg_autre','login_description','register_description','contact_description','admission_description','description_cours','single_cours_titre','single_cours_description','single_news_titre']}),
          ('standard', {'fields':['status']}),
          ]
    def logo_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.logo.url))

    def caracteristique_bg_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.caracteristique_bg.url))

    def newletter_bg_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.newletter_bg.url))

    def about_image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.about_image.url))


    def logo_footer_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.logo_footer.url))

    def bg_autre_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.bg_autre.url))

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'


@admin.register(models.Newletter)
class NewletterAdmin(admin.ModelAdmin):
    list_display = ('email','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('email',)
    date_hierarchy = 'date_add'
    list_display_links = ['email']
    fieldsets = [
    ('Newletter_info', {'fields':['email']}),
    ('standard', {'fields':['status']}),
    ]

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'


@admin.register(models.Aboutt)
class AbouttAdmin(admin.ModelAdmin):
    list_display = ('titre','date_add','date_update','status','image_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
          ('About_info', {'fields':['titre','description','description2','image']}),
          ('standard', {'fields':['status']}),
          ]
    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','email','telephone','message','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('firstname',)
    date_hierarchy = 'date_add'
    list_display_links = ['firstname']
    fieldsets = [
          ('Contact_info', {'fields':['firstname','lastname','email','telephone','message',]}),
          ('standard', {'fields':['status']}),
          ]

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Slice)
class SliceAdmin(admin.ModelAdmin):
    list_display = ('titre','date_add','date_update','status','image_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
          ('slice_info', {'fields':['titre','image']}),
          ('standard', {'fields':['status']}),
          ]
    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Caracteristique)
class CaracteristiqueAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('Caracteristique_info', {'fields':['nom','description']}),
          ('standard', {'fields':['status']}),
          ]

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Enseignant)
class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('nom','matiere','date_add','date_update','status','photo_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('Enseignant_info', {'fields':['nom','matiere','biographie','photo']}),
          ('standard', {'fields':['status']}),
          ]
    def photo_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.photo.url))


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Reseau_social)
class Reseau_socialAdmin(admin.ModelAdmin):
    list_display = ('nom','lien','icone','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('Reseau_social_info', {'fields':['nom','lien','icone',]}),
          ('standard', {'fields':['status']}),
          ]

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('nom','fonction','date_add','date_update','status','photo_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('Temoignage_info', {'fields':['nom','fonction','Temoignage','photo']}),
          ('standard', {'fields':['status']}),
          ]

    def photo_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.photo.url))


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'
