
from django.shortcuts import render, redirect
import os
from twilio.rest import Client
from .forms import CommandeForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Article, Commande
from django.contrib import messages
from twilio.rest import Client
# Create your views here.
def home(request): # parametre request obligatoire qui va permettre les requettes http
    list_article=Article.objects.all() # tu recupere tout les objets de la classe article pour mettre dans list_article
    context={"liste_articles":list_article}

    return render(request,"index.html",context)# veut dire tu m'envoi un templates appellé index.html
    # je vais dans mon dossier charo pour creer un dossier templates
    # render permet de rendre le fichier html au user et tu vas le rendre avec context


def search(request):
    #GET={"article":"cafe"} c'est ce qui ce passe dans la ligne juste apres
    query=request.GET["article"]
    liste_article=Article.objects.filter(nom__icontains=query) # tu vas selectioner tout les objets dont le titre est egale à qruery
    return render(request,"search.html",{"liste_articles":liste_article})
    # les ypes de requettes : SELECT *FROM Article where titre LIKE %'query'% veut dit que si il ya des mot dans la demande de l'utilisateur et que notre titre est dedans on envoi la requettes







def recup(request, id_commande):
    commande = Commande.objects.get(id=id_commande)
    article = commande.article
    nom_client = commande.nom_client
    num_client = commande.numero_client
    quantite = commande.quantite
    
    
    context = {
        "nom_client": nom_client,
        "nom_article": article.nom,
        "quantite": quantite,
        "numero_client": num_client,
        "total": (article.prix * quantite) 
    }

       

    


    


    return render(request, "effectuer.html", context)




class CommandeCreateView(CreateView):
    model = Commande
    form_class = CommandeForm
    template_name = 'comande.html'
    success_url = reverse_lazy("afficher", kwargs={'id_commande': None})

    def get_success_url(self):
        return reverse_lazy("afficher", kwargs={'id_commande': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_id = self.kwargs['id_article']
        article = Article.objects.get(id=article_id)
        context['article'] = article
        return context

    def form_valid(self, form):
        numero_client = form.cleaned_data['numero_client']
        
        if len(numero_client) == 10:
            article_id = self.kwargs['id_article']
            article = Article.objects.get(id=article_id)
            form.instance.article = article
            return super(CommandeCreateView, self).form_valid(form)
        else:
            messages.error(self.request, "Numéro incorrect. Veuillez entrer un numéro de 10 chiffres.")
            
            return super(CommandeCreateView, self).form_valid(form)




# Download the helper library from https://www.twilio.com/docs/python/install
