from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm


class ContactCreate(CreateView):
    model = Contact
    # fields = ["first_name", "last_name", "message"]
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

    def form_valid(self, form):

        data = form.data
        subject = f'Сообщение с формы от {data["first_name"]} {data["last_name"]} Почта отправителя: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)


def email(subject, content):
   send_mail(subject,
      content,
      'отправитель@gmail.com',
      ['получатель1@gmail.com']
   )


def success(request):
   return HttpResponse('Письмо отправлено!')