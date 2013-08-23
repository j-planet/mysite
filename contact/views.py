from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from forms import ContactForm


def contact(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_dta

            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )

            return HttpResponseRedirect('templates/thanks/')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})