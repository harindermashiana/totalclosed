from django import forms

class FileFieldForm(forms.Form):
    file_field = forms.ImageField(label = 'Choose your image',
                                          help_text = 'The image should be cool.')