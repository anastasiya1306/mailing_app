from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import CustomerForm, MessageForm
from main.models import Customer, Message, Mailing


class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Главная страница'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomerListView(ListView):
    model = Customer
    extra_context = {
        'title': 'Клиенты'
    }


class CustomerDetailView(DetailView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('main:customer_list')


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('main:customer_list')


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('main:customer_list')


class MessageListView(ListView):
    model = Message
    extra_context = {
        'title': 'Сообщения'
    }


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('main:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('main:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('main:message_list')


class MailingListView(ListView):
    model = Mailing
    extra_context = {
        'title': 'Рассылки'
    }


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('mailing_time', 'message', 'frequency', 'status',)
    success_url = reverse_lazy('main:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('message', 'frequency', 'status', )
    success_url = reverse_lazy('main:mailing_list')


class MailingDetailView(DetailView):
    model = Mailing


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('main:mailing_list')
