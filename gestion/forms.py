from django import forms
from .models import Commande,Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["nom", "description", "prix", "photo1", "photo2"]
        labels = {
            "nom": "Nom",
            "description": "Description",
            "prix": "Prix",
            "photo1": "Photo 1",
            "photo2": "Photo 2",
           
        }
        widgets = {
            "nom": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "prix": forms.NumberInput(attrs={"class": "form-control"}),
            "photo1": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "photo2": forms.ClearableFileInput(attrs={"class": "form-control"}),
           
        }





class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['nom_client', 'numero_client', 'quantite','taille']
        labels = {
            'nom_client': 'Nom',
            'numero_client': 'Numéro de téléphone',
            'quantite': 'Quantité',
            'taille': 'Taille',
           

            
            
        }
