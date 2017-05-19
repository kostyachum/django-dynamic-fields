# Django Dynamic Fields
An applications that extends your Django Model and allow to customize field list from admin.
 
## Usage

### Model
```python
from django.db import models
from django.conf import settings

from dynamic_fields.models import DynamicFieldsModel


class Customer(DynamicFieldsModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    address = models.CharField(max_length=255)

```


### Form
```python
from example.models import Customer
from dynamic_fields.forms import CustomFieldsForm


class CustomerForm(CustomFieldsForm):
    class Meta:
        model = Customer
        fields = '__all__'

```


### Template
```jinja2
{%  extends "base.html" %}


{% block content %}
    <form method="post" >
    {% csrf_token %}
        {{  form.as_p }}
    <button type="submit">SAVE</button>
    </form>
{% endblock %}
```


### Customize
- Go to admin /admin/dynamic_fields/field/
- Add fields
