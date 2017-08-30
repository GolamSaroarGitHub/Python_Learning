from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=('first_description','first_document','second_description','second_document')