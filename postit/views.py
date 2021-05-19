from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from postit.models import Note
from django.views import View

# Create your views here.

class IndexListView(ListView):
    model = Note
    template_name = 'postit/index.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.all().order_by('-id')

def add_note(request):
    if request.method == 'POST':
        note = request.POST.get('note')
        alias = request.POST.get('alias')
        #create new Object
        note = Note(
            alias = alias,
            note = note
        )
        note.save()
        return redirect('postit:index')

def del_all(request):
    notes = Note.objects.all()
    for i in notes:
        i.delete()
    return redirect('postit:index')

def mark_all(request):
    notes = Note.objects.all()
    for i in notes:
        i.status = 'm'
        i.save()
    return redirect('postit:index')

def unmark_all(request):
    notes = Note.objects.all()
    for i in notes:
        i.status = 'u'
        i.save()
    return redirect('postit:index')

def update_note(request):
    if request.method == "POST":
        alias = request.POST.get('alias')
        note = request.POST.get('note')
        id = request.POST.get('id')
        note_obj = get_object_or_404(Note, id=id)
        note_obj.alias = alias
        note_obj.note = note
        note_obj.save();
        return redirect('postit:index')


