from django.contrib import admin
from .models import Book
# Register your models here.

#this class allows to set various options that will be reflected on admin page
class BookAdmin(admin.ModelAdmin):
    #field will be read only
    #readonly_fields=("slug",)  

    #automatically populate the field but will not work if readonly_fields is also applied onthe used field
    prepopulated_fields ={"slug":("title",)} # tuple listing all the fields that should be used
    
    #make list filterable by the selected fields
    list_filter =("author","rating",)

    #display selected fields on the admin page
    list_display=("title","author",)

#tells django that this model and class should be added to the administrative site
admin.site.register(Book,BookAdmin)