from django import forms

from ..models.user import User


class UserSelectForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        help_text='select the user you want to add as a contributor',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        excludes = kwargs.pop('excludes', None)
        super().__init__(*args, **kwargs)

        if excludes:
            self.fields['user'].queryset = User.objects.exclude(pk__in=[e.pk for e in excludes])

    def clean(self):
        data = self.cleaned_data
        if 'user' not in data.keys():
            raise forms.ValidationError('you must specify a user')

        user = User.objects.filter(username=data['user']).first()
        if not user:
            raise forms.ValidationError('that user somehow doesn\'t exist... something must have gone wrong.')

        data['user'] = user
        return data


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('preferred_name',)
