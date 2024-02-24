from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.db.models import Avg
#get the Book from the models file
from .models import Book

# Create your views here.
def index(request):
    #query your data but it is not recommended to perform more than one query
    books=Book.objects.all().order_by("title")#fetch all data
    ### AGGREGATE METHODS ###
    #get aggregate data
    num_books=books.count()
    avg_rating = books.aggregate(Avg("rating")) #get the average of rating in dictionary format 
    return render(request,"book_outlet/index.html",{
        "books":books,
        "total_number_of_books":num_books,
        "average_rating":avg_rating
    })

def book_detail(request,slug):
    #### COMMON PATTERN #####
    #try:
    #query that gets data that matches the id
    #    book=Book.objects.get(pk=id) # pk can be used to get the primary ket
    #except:
    #    raise Http404()
    ##############################

    #### ALTERNATIVE ####
    book=get_object_or_404(Book,slug=slug)

    return render(request,"book_outlet/book_detail.html",{
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestseller":book.is_bestselling})