from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

# Home: View all notes (latest first)
from django.db.models import Q  # Import Q for advanced querying

@login_required
def home(request):
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            user=request.user
        ).order_by('-created_at')  # Newest notes first
    else:
        notes = Note.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, 'notes/home.html', {'notes': notes})


# Add a new note
@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})


# Edit an existing note

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    return render(request, 'notes/delete_note.html', {'note': note})

