from django.shortcuts import render, redirect
from .forms import ContactUsForm
from .models import ContactUs
from .forms import *


def contact_us_view(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        # contact_form = ContactUsModelForm(request.POST)
        if contact_form.is_valid():
            contact = ContactUs(
                title=contact_form.cleaned_data.get('title'),
                full_name=contact_form.cleaned_data.get('full_name'),
                email=contact_form.cleaned_data.get('email'),
                message=contact_form.cleaned_data.get('message'),
            )

            contact.save()
            # contact_form.save()  # model forms

            return redirect('core:index')

    else:
        contact_form = ContactUsForm()
        # contact_form = ContactUsModelForm()
    context = {
        'contact_form': contact_form
    }
    return render(request, 'contact_us/contact_us.html', context=context)
