from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm




def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/members/login')
    context = {'form':form}
    return render(request, "registration/register.html", context)