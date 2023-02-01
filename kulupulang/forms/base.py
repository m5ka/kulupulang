from django.forms import ModelForm


class BaseModelForm(ModelForm):
    error_css_class = "error"
    required_css_class = "required"
