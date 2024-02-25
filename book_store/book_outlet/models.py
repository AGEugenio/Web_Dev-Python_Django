from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify #transform a text into a slug
# Create your models here.
# blueprints for the data objects of application will be here

class Book(models.Model):
    #define the structure of the single book
    title = models.CharField(max_length=50) 
    rating = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.CharField(null=True,max_length=100)
    is_bestselling = models.BooleanField(null=False,default=False)
    #id = models.AutoField() - this is automatically added to every data entity by Django
    
    # slug format like Harry Potter 1 => harry-potter-1
    slug = models.SlugField(default="",blank=True,null=False, db_index=True) #db_index add database index in the field, db will save the field more efficient
    #this can make searching that field quicker; recommended to only used this to commonly used field


    #you can add methods to custom logic and override some built-in method
    def get_absolute_url(self): #this is usually automatically load by django
        return reverse("book-detail", args=[self.slug]) # gets the slug arg in url
    
    #### THIS CAN BE REMOVED SINCE THE CREATED CLASS IN ADMIN.PY OVERRIDES THIS ###
    #override the save method
    def save(self, *args, **kwargs): #standard Python Syntax
        #group all positional and all keyword arguments into a summary parameter: args and kwargs

        #before the data is saved to the database
        self.slug=slugify(self.title) #transform the title into  slug format
       
        #should call this to ensure that Django built in save method is still getting called
        super().save(*args, **kwargs) # make sure to also pass the parameters
    ######################################################################################
        
    #a method that can be used to define how object is returned
    def __str__(self):
        return f"{self.title}({self.rating})"

