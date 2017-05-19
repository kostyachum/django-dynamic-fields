import json

from django import forms

from . import config
from .models import Field


class CustomFieldsForm(forms.ModelForm):
    """
    Adds fields from custom fields model to the form, saves to `custom_field_data` of an instances
    
    Set meta for your form:
    >>>class Meta:
    >>>    model = Customer
    >>>    fields = '__all__'
    """

    def __init__(self, *args, **kwargs):
        self.generate_fields()
        super(CustomFieldsForm, self).__init__(*args, **kwargs)
        self.init_custom_fields_data()

    def generate_fields(self):
        """
        Generates field instances for the the form from the custom fields queryset        
        """
        for custom_field in self.get_custom_fields():
            field_instance = config.FIELDS_MAPS.get(custom_field.type)()
            field_instance.is_custom = True
            field_instance.required = custom_field.required
            if custom_field.type == config.DROPDOWN_FIELD:
                choice_values = custom_field.choices.all().values_list('value', flat=True)
                field_instance.choices = zip(choice_values, choice_values)
            self.base_fields[custom_field.name] = field_instance

    def init_custom_fields_data(self):
        """
        Sets initial data for the custom fields from the "custom_field_data" instance field
        """
        print('self.instance.custom_field_data', self.instance.custom_field_data)
        if self.instance and self.instance.custom_field_data:
            custom_data = json.loads(self.instance.custom_field_data)
            for field in self.fields:
                if getattr(self.fields[field], 'is_custom', False):
                    self.fields[field].initial = custom_data.get(field)

    def get_custom_fields(self):
        """
        Returns list of custom field instances
        :return: queryset CustomField
        """
        return Field.objects.all()

    def set_custom_field_data(self):
        """
        Generates dict from custom fields and dumps JSON to custom_field_data instance field
        """
        custom_field_dict = {}
        for key, value in self.cleaned_data.items():
            if getattr(self.fields[key], 'is_custom', False):
                custom_field_dict[key] = value
        self.instance.custom_field_data = json.dumps(custom_field_dict)

    def save(self, commit=True):
        self.set_custom_field_data()
        return super(CustomFieldsForm, self).save(commit=commit)
