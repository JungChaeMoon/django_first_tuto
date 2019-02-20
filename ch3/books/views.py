from django.shortcuts import render

# Create your views here.

from books.models import Book, Author, Publisher
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

class BooksModelView(TemplateView):

    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context

class BookList(ListView):
    model = Book
"""
def BookList(request):
    book_list = Book.object.all()
    context = {'book_list' : book_list}
    return
        render(request, 'book/book_list.html', context)
"""
class AuthorList(ListView):
    model = Author

class PublisherList(ListView):
    model = Publisher

class BookDetail(DetailView):
    model = Book

class AuthorDetail(DetailView):
    model = Author

class PublisherDetail(DetailView):
    model = Publisher

