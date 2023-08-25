from django.forms import ModelForm, TextInput, Textarea, NumberInput, CheckboxInput, FileInput
from .models import Avito
from django.core.exceptions import ValidationError


class AvitoForm(ModelForm):
    class Meta:
        model = Avito
        fields = ['title', 'description', 'price', 'auction', 'image']

        widgets = {

            "title": TextInput(attrs={
                "class": "form-control form-control-lg",
            }),

            "description": Textarea(attrs={
                "class": "form-control form-control-lg",
            }),

            "price": NumberInput(attrs={
                "class": "form-control form-control-lg",
            }),

            "auction": CheckboxInput(attrs={
                "class": "form-check-input",
            }),

            "image": FileInput(attrs={
                "class": "form-control form-control-lg",
            }),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина превышает 50 символов!')
        elif title[0] == '?' or title[0] == '!':
            raise ValidationError('Название не может начинаться с этого знака!')
        return title