# Create your views here.

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from django.urls import reverse_lazy

from .models import Note


class NoteListView(ListView):
    model = Note
    template_name = "notes_list.html"


class NoteCreateView(CreateView):
    model = Note
    template_name = "note_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("notes_list")


class NoteUpdateView(NoteCreateView, UpdateView):
    pass


class NoteDetailView(DetailView):
    model = Note
    template_name = "note_detail.html"


class NoteDeleteView(DeleteView):
    model = Note
    template_name = "note_delete.html"
    success_url = reverse_lazy("notes_list")
