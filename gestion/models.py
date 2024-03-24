from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import RegexValidator
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    nom_category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    photo1 = models.ImageField(null=True,blank=True)
    photo2 = models.ImageField(null=True,blank=True)
    exemplaires_disponibles = models.IntegerField(null=True, blank=True)
    
    def nombre_exemplaires_epuises(self):
        epuisee=self.commande_set.filter(statut='livre').count()
        return epuisee
    

    def nombre_exemplaires_restants(self):
         
        restante=self.exemplaires_disponibles - self.nombre_exemplaires_epuises()
        return restante
    

    def __str__(self):
        return self.nom
    def get_absolute_url(self):
        return reverse("commande") 
    
    def get_absolute_url(self):
        return reverse("my-article") 

class Commande(models.Model):
    TAILLE_CHOICES = [
        ('X', 'X'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('M', 'M'),
    ]
    
    STATUT_CHOICES = [
        ('en_cours', 'En cours'),
        ('livre', 'Livrée'),
    ]
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    nom_client = models.CharField(max_length=100)
    numero_client = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',  # Format: 10 chiffres
            )
        ]
    )
    quantite = models.PositiveIntegerField()
    taille = models.CharField(max_length=3, choices=TAILLE_CHOICES, default='null')
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='en_cours')
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande de {self.quantite} {self.article.nom} ({self.get_taille_display()}) par {self.nom_client}"



    
