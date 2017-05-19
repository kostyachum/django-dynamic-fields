from example.models import Customer
from dynamic_fields.forms import CustomFieldsForm


class CustomerForm(CustomFieldsForm):
    class Meta:
        model = Customer
        fields = '__all__'
