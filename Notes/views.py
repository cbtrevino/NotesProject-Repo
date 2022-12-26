from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NoteForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

def editor(request):
    form = NoteForm(request.POST)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return HttpResponseRedirect('/home')
    else:
        form = NoteForm
    return render(request, 'editor.html', {'form': form})

