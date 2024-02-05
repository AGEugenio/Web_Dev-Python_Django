from django.urls import path

from . import views
# list for all url patterns we want
urlpatterns = [
    
    #starting page which lists latest blog posts and welcome text
    path("",views.starting_page,name="starting-page"),
    #load page which lists all blog posts
    path("posts",views.posts,name="posts-page"),
    #load individual page
    path("posts/<slug:slug>",views.post_detail,name="post-detail-page") #/posts/this-concept-is-called-slug; search engine friendly identifier

]