from django.shortcuts import render, redirect
from .models import *
from .forms import BookForm, CategoryForm

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    context ={
        'books': Book.objects.all(),
        'categories':Category.objects.all(),
        'forms': BookForm(),
        'categoryform': CategoryForm(),
        'allbooks':Book.objects.filter(active=True).count(),
        'booksold':Book.objects.filter(status='sold').count(),
        'bookrental':Book.objects.filter(status='rental').count(),
        'bookavailable':Book.objects.filter(status='available').count(),
        'bookavailable':Book.objects.filter(status='available').count(),

    }
    return render(request, 'pages/index.html', context)

def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains = title)
    context ={
        'books': search,
        'categories':Category.objects.all(),
        'categoryform': CategoryForm(),
    }
    return render(request, 'pages/books.html',context)

# Get book by id and update
def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method =='POST':
        update_book = BookForm(request.POST, request.FILES, instance=book_id)
        if update_book.is_valid():
            update_book.save()
            return redirect('/')
    else:
        update_book = BookForm(instance=book_id)
    context = {
        'form':update_book,
    }
    return render(request ,'pages/update.html', context)

# Get book by id and delete it
def delete(request, id):
    delete_book = Book.objects.get(id=id)
    if request.method == 'POST':
        delete_book.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')
