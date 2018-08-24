from django.shortcuts import render

from notes.models import Note


def notes(request):
    notes = Note.objects.filter().order_by('-created')
    return render(request, 'notes.html', {'notes': notes})
