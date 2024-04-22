from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from common.models import Software
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import ContactForm
from django.conf import settings
from django.views.generic import FormView

def home(request):
    promoted_downloads = Software.objects.filter(promot_to_front=True)
    context = {
        'downloads' : promoted_downloads
    }
    return render(request, 'common/home.html', context)


def downloads(request):
    downloads = Software.objects.all()
    context = {
        'downloads' : downloads
    }
    return render(request, 'common/downloads.html', context)


def download_software(request, file_id):
    file_obj = get_object_or_404(Software, pk=file_id)
    return FileResponse(open(file_obj.file.path, 'rb'))




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # Send email to user
            user_subject = 'ShamukSoft-Thank you for contacting us!'
            user_html_message = render_to_string('emails/user_contact_email.html', {'name': form.cleaned_data['name']})
            user_plain_message = strip_tags(user_html_message)
            
            send_mail(
                user_subject, 
                user_plain_message, 
                settings.EMAIL_HOST_USER, 
                [form.cleaned_data['email']], 
                html_message=user_html_message
            )

            # Send email to admin
            admin_subject = 'MrShamuk-New contact submitted'
            admin_html_message = render_to_string(
                'emails/admin_email.html', 
                {
                    'name': form.cleaned_data['name'], 
                    'email': form.cleaned_data['email'], 
                    'message': form.cleaned_data['message']
                }
            )
            admin_plain_message = strip_tags(admin_html_message)
            send_mail(
                admin_subject, 
                admin_plain_message, 
                settings.EMAIL_HOST_USER, 
                [settings.ADMIN_EMAIL], 
                html_message=admin_html_message
            )

            return redirect('common:success')
    else:
        form = ContactForm()
    return render(request, 'common/contact.html', {'form': form})

def success_view(request):
    return render(request, 'common/success.html')