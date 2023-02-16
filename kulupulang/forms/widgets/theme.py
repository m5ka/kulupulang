from django.forms.widgets import RadioSelect

from kulupulang.models.theme import Theme


class ThemeSelect(RadioSelect):
    template_name = "kulupulang/widgets/theme_select.jinja"
