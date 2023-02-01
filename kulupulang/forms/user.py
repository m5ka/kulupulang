from django import forms
from django.conf import settings

from ..models.user import User


class UserSelectForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        help_text="select the user you want to add as a contributor",
        required=True,
    )

    def __init__(self, *args, **kwargs):
        excludes = kwargs.pop("excludes", None)
        super().__init__(*args, **kwargs)

        if excludes:
            self.fields["user"].queryset = User.objects.exclude(
                pk__in=[e.pk for e in excludes]
            )

    def clean(self):
        data = self.cleaned_data
        if "user" not in data.keys() or not data["user"]:
            raise forms.ValidationError("you must specify a user")
        return data


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "preferred_name",
            "theme",
        )
        widgets = {"theme": forms.Select(choices=settings.KULUPULANG_USER_THEMES)}
