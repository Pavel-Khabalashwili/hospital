from .models import Applications
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput

class ApplicationsForm(ModelForm):
    class Meta:
        model = Applications
        fields = ['title', 'desk', 'status', 'image']

        widgets = {
            "title": TextInput(attrs={
                'class': 'apl-form__input section-descr',
                'placeholder': 'Заголовок'
            }),
            "desk": Textarea(attrs={
                'class': 'apl-form__txt',
                'placeholder': 'Описание'
            }),
            "status": TextInput(attrs={
                'class': 'apl-form__input section-descr',
                'placeholder': 'Текущее состояние'
            }),
            "image": ClearableFileInput(attrs={
                'class': 'field field__file',
                'id': 'field__file-2'
            })
        }