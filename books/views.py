from django.views import generic
from .models import Book


class BookListView(generic.ListView):
    template_name = 'books/book_list.html'
    model = Book
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    template_name = 'books/book_detail.html'
    model = Book


class BookCreateView(generic.CreateView):
    template_name = 'books/book_create.html'
    model = Book
    fields = '__all__'
