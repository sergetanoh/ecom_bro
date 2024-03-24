from django.shortcuts import render,redirect
from gestion.models import Article,Commande
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from gestion.forms import ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseBadRequest


def dashboard(request):
    return render (request,'db.html')

def search(request):
    #GET={"article":"cafe"} c'est ce qui ce passe dans la ligne juste apres
    query=request.GET["commande"]
    liste_commandes=Commande.objects.filter(date_commande__icontains=query) # tu vas selectioner tout les objets dont le titre est egale à qruery
    return render(request,"voir-article.html",{"liste_commandes":liste_commandes})
    # les ypes de requettes : SELECT *FROM Article where titre LIKE %'query'% veut dit que si il ya des mot dans la demande de l'utilisateur et que notre titre est dedans on envoi la requettes


def user_article(request):
    if not request.user.is_superuser: # si l'utilisateur n'est pas connecte et veut acceder a l'espace admin on refuse
        return redirect('login-blog')
    list_article=Article.objects.all()
    Comande = Commande.objects.all()
    context={'list_articles':list_article,'liste_commande':Comande}
    return render(request,'my-article.html',context)


class Add_article(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "add-article.html"
    success_url = "my-article"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class update_article(LoginRequiredMixin,UpdateView):
    model=Article
    form_class=ArticleForm
    template_name="app_admin/article_form.html"

    
class delete_article(LoginRequiredMixin,DeleteView):
    model=Article
    success_url='../my-article'
    template_name="app_admin/article_confirm_delete.html"


class delete_commande(LoginRequiredMixin,DeleteView):
    model=Commande
    success_url='../my-article'
    template_name="app_admin/commande_confirm_delete.html"
    
    