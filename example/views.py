from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from .models import Customer
from .forms import CustomerForm


class CustomerFormView(CreateView):
    template_name = 'form.html'
    form_class = CustomerForm
    model = Customer

    def get_success_url(self):
        return reverse('customer-details', args=[self.object.pk])

    def form_valid(self, form):
        form.save()
        return super(CustomerFormView, self).form_valid(form)


class CustomerDetailView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('customer-details', args=[self.object.pk])

    def form_valid(self, form):
        form.save()
        return super(CustomerDetailView, self).form_valid(form)
