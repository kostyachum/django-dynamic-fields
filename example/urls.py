from django.conf.urls import url
from example.views import CustomerFormView, CustomerDetailView

urlpatterns = [
    url(r'^add/$', CustomerFormView.as_view()),
    url(r'^edit/(?P<pk>[0-9]+)$', CustomerDetailView.as_view(), name='customer-details')
]
