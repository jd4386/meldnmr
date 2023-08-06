from django.shortcuts import render
from .forms import RequestModelForm
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.conf import settings

def index(request):
    submitted = False

    if request.method == 'POST':
        form = RequestModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            email = EmailMessage(
                'New request',
                'A new request has been submitted with the following file attached.',
                settings.EMAIL_HOST_USER,
                [request.POST['email']],
            )

            email.attach_file('media/files/' + request.FILES['file'].name)
            email.send()

            return HttpResponseRedirect('/?submitted=True')
    else:
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/index.html', {'form': {}, 'submitted': submitted})
