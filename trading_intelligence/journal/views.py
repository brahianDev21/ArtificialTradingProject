from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import JournalForm
from .models import Journal

@login_required
def create_journal(request):
    if request.method == 'POST':
        form = JournalForm(request.POST, request.FILES)
        if form.is_valid():
            journal_entry = form.save(commit=False)
            journal_entry.user = request.user
            journal_entry.save()
            messages.success(request, 'Journal entry created successfully.')
            return redirect('journal_entries')
        
    else:

        form = JournalForm()

    return render(request, 'journal/create_journal.html', {'form': form})

@login_required
def journal_entries(request):
    user_journals = Journal.objects.filter(user=request.user) 
    return render(request, 'journal/journal_entries.html', {'journals': user_journals})

@login_required
def journal_detail(request, journal_id):

    journal_entry = get_object_or_404(Journal, id=journal_id)

    
    if journal_entry.user != request.user:
        messages.error(request, "No tienes permiso para ver esta entrada")
        return redirect('journal_entries')  

    
    return render(request, 'journal/journal_detail.html', {'journal': journal_entry})

@login_required
@require_POST  
def delete_journal(request, journal_id):
    journal_entry = get_object_or_404(Journal, id=journal_id)

    
    if journal_entry.user != request.user:
        messages.error(request, "No tienes permiso para eliminar esta entrada")
        return redirect('journal_entries')  

    journal_entry.delete()  
    messages.success(request, "Entrada eliminada exitosamente")
    return redirect('journal_entries') 

@login_required
def edit_journal(request, journal_id):
    journal_entry = get_object_or_404(Journal, id=journal_id, user=request.user)

    if request.method == 'POST':
        form = JournalForm(request.POST, request.FILES, instance=journal_entry)
        if form.is_valid():
            form.save()
            messages.success(request, "Journal editado exitosamente")
            return redirect('journal_entries')
    else:
        form = JournalForm(instance=journal_entry)

    return render(request, 'journal/edit_journal.html', {'form': form, 'journal': journal_entry})