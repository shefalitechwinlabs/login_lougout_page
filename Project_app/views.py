from django.shortcuts import render
from django.http import HttpResponse
from Project_app.models import Author, Book, Publisher
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from django.template import loader
from authentication import views as auth_v
from django.contrib.auth.models import User

def home(request):
    if 'username' in request.session:
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect('/')


def form(request):
    if 'username' in request.session:
        if request.method=="POST":
            author_name = request.POST["author_name"]
            #publisher_name = request.POST["publisher_name"]
            title = request.POST["title"]
            genre = request.POST["genre"]
            #author = request.Author.author_name
            #country = request.POST["country"]
            #author = request.POST["author"]
            #publisher = request.POST["publisher"]
            #publication_date = request.POST["publication_date"]
            username = request.user
            #print(author_name,user)
            #print(author)
            A = Author(author_name=author_name,user=username)
            A.save()
            B = Book(title=title,genre=genre)
            B.save()
            B.author.add(A)
            B.save()
        return render(request, 'form.html')
    else:
        return HttpResponseRedirect('/')



def table(request):
    if "username" in request.session:
        context = {}
        username = request.user
        author = Author.objects.get(user=username)
        context['Book'] = Book.objects.filter(author=author)
        context['Author'] = Author.objects.filter(user=username).values()
        print(type(context['Author']))
        print(type(context['Book']))
        return render(request, 'table.html', context)
    else:
        return HttpResponseRedirect('/')




def delete(request,id):
    
    if "username" in request.session:
        obj = get_object_or_404(Author, id = id)
        
        if request.method =="POST":
            # delete object
            obj.delete()
            return HttpResponseRedirect("/home/table")
        
        return render(request, "delete.html")
    else:
        return HttpResponseRedirect('/')



def update_table(request, id):
    
    if "username" in request.session:
        objects = get_object_or_404(Author,id=id) 

        if request.method=="POST":
            author_name = request.POST["author_name"]
            #publisher_name = request.POST["publisher_name"]
            title = request.POST["title"]
            genre = request.POST["genre"]
            #country = request.POST["country"]
            #author = request.POST["author"]
            #publisher = request.POST["publisher"]
            #publication_date = request.POST["publication_date"]
            objects.author_name = author_name
            #objects.publisher_name = publisher_name
            objects.title = title
            objects.genre = genre
            #objects.country = country
            #objects.author = author
            #objects.publisher = publisher
            #objects.publication_date = publication_date
            objects.save()
            return HttpResponseRedirect("/home/table")
        
        data = {}
        data["dataset"] = Author.objects.all().filter(id=id)
        
        return render(request, "update.html", data)
    else:
        return HttpResponseRedirect('/')