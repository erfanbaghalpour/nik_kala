from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactUsForm
from .models import ContactUs
from .forms import *


# class ContactUsView(View):
#     def get(self, request):
#         contact_form = ContactUsModelForm()
#         context = {
#             'contact_form': contact_form
#         }
#         return render(request, 'contact_us/contact_us.html', context=context)
#
#     def post(self, request):
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect('core:index')
#         context = {
#             'contact_form': contact_form
#         }
#         return render(request, 'contact_us/contact_us.html', context=context)

# def contact_us_view(request):
#     if request.method == 'POST':
#         contact_form = ContactUsForm(request.POST)
#         # contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             contact = ContactUs(
#                 title=contact_form.cleaned_data.get('title'),
#                 full_name=contact_form.cleaned_data.get('full_name'),
#                 email=contact_form.cleaned_data.get('email'),
#                 message=contact_form.cleaned_data.get('message'),
#             )
#
#             contact.save()
#             # contact_form.save()  # model forms
#
#             return redirect('core:index')
#
#     else:
#         contact_form = ContactUsForm()
#         # contact_form = ContactUsModelForm()
#     context = {
#         'contact_form': contact_form
#     }
#     return render(request, 'contact_us/contact_us.html', context=context)


class ContactUsView(FormView):
    template_name = 'contact_us/contact_us.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
