from django.views import generic
from .models import Book
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy


class BookListView(generic.ListView):
    template_name = 'books/book_list.html'
    paginate_by = 4
    model = Book
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     template_name = 'books/book_detail.html'
#     model = Book

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all().order_by('-datetime_created')
    return render(request, 'books/book_detail.html', {'book': book, "comments": comments})


class BookCreateView(generic.CreateView):
    template_name = 'books/book_create.html'
    model = Book
    fields = '__all__'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'books/book_update.html'

    def form_valid(self, form):
        if form.has_changed():
            form.save()
            return redirect('book_detail', pk=self.object.pk)
        else:
            return redirect('book_update', pk=self.object.pk)


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
