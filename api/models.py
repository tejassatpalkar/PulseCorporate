from django.db import models

# Create your models here.
# fat models thin views. logic goes here


class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    past_sponsorship = models.IntegerField(default=0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name



class Contact(models.Model):

    #required
    first_name = models.CharField(max_length=30) 
    email = models.EmailField(max_length=254)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='contact')

    #automatically handled
    created = models.DateTimeField(auto_now_add=True)
    last_changed = models.DateTimeField(auto_now=True)
    # not explicitly required
    
    last_name = models.CharField(max_length=30, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




