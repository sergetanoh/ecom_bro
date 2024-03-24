from django.contrib import admin
from .models import Article,Commande,Category
# Register your models here.
#admin.site.register(Article)
#admin.site.register(Commande)
admin.site.register(Category)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'prix', 'exemplaires_disponibles', 'nombre_exemplaires_epuises', 'nombre_exemplaires_restants')

    def nombre_exemplaires_epuises(self, obj):
        return obj.nombre_exemplaires_epuises()

    def nombre_exemplaires_restants(self, obj):
        return obj.nombre_exemplaires_restants()

admin.site.register(Article, ArticleAdmin)




class CommandeAdmin(admin.ModelAdmin):
    list_display = ('article', 'nom_client', 'numero_client', 'quantite','taille', 'statut', 'date_commande')

admin.site.register(Commande, CommandeAdmin)
