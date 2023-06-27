from django.shortcuts import render
from .forms import RequestModelForm
from django.http import HttpResponseRedirect

def index(request):
    submitted = False

    if request.method == 'POST':
        form = RequestModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/?submitted=True')
    else:
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/index.html', {'form': {}, 'submitted': submitted})
