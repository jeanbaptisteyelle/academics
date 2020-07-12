from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.
@admin.register(models.Caracteristique)
class CaracteristiqueAdmin(admin.ModelAdmin):
    list_display = ('nom','icone','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
    ('Caracteristique_info', {'fields':['nom','description','icone',]}),
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
    desactive.short_description = 'activer'

@admin.register(models.Domaine)
class DomaineAdmin(admin.ModelAdmin):
    list_display = ('titre','prix','heure_debut','heure_fin','date_add','date_update','status','image_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
    ('Domaine_info', {'fields':['titre','prix','description','heure_debut','heure_fin','image','content']}),
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
    desactive.short_description = 'activer'

@admin.register(models.Cour)
class CourAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status')
    list_filter = ('date_add','date_update','status','domaine')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
    ('Cour_info', {'fields':['nom','domaine']}),
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
    desactive.short_description = 'activer'

@admin.register(models.Admisssion)
class AdmisssionAdmin(admin.ModelAdmin):
    list_display = ('note','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('note',)
    date_hierarchy = 'date_add'
    list_display_links = ['note']
    fieldsets = [
    ('Admission_info', {'fields':['note','content']}),
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
    desactive.short_description = 'activer'


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('titre','date_add','date_update','status','image_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
    ('Cour_info', {'fields':['titre','image','description']}),
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
    desactive.short_description = 'activer'

@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titre','lien','date_add','date_update','status','image_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre','image_view']
    fieldsets = [
    ('Video_info', {'fields':['titre','lien','description','image']}),
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
    desactive.short_description = 'activer'

