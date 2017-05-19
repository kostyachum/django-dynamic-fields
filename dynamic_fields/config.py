from django import forms

DATETIME_FIELD = 1
DATE_FIELD = 2
CHAR_FIELD = 3
INT_FIELD = 4
FLOAT_FIELD = 5
FILE_FIELD = 6
IMAGE_FIELD = 7
TEXT_FIELD = 8
EMAIL_FIELD = 9
DROPDOWN_FIELD = 10

FIELD_TYPES = (
    (DATETIME_FIELD, 'Date time'),
    (DATE_FIELD, 'Date'),
    (CHAR_FIELD, 'Char'),
    (INT_FIELD, 'Integer'),
    (FLOAT_FIELD, 'Float'),
    (FILE_FIELD, 'File'),
    (IMAGE_FIELD, 'Image'),
    (TEXT_FIELD, 'Text'),
    (EMAIL_FIELD, 'Email'),
    (DROPDOWN_FIELD, 'Dropdown'),
)

FIELDS_MAPS = {
    DATETIME_FIELD: forms.DateTimeField,
    DATE_FIELD: forms.DateField,
    CHAR_FIELD: forms.CharField,
    INT_FIELD: forms.IntegerField,
    FLOAT_FIELD: forms.FloatField,
    FILE_FIELD: forms.FileField,
    IMAGE_FIELD: forms.ImageField,
    TEXT_FIELD: forms.CharField,
    EMAIL_FIELD: forms.EmailField,
    DROPDOWN_FIELD: forms.ChoiceField,
}
