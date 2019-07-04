from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['phone'].widget.attrs['pattern'] = "^(\+375|80)(29|25|44|33)(\d{3})(\d{2})(\d{2})$"
        self.fields['phone'].widget.attrs['placeholder'] = "(+375|80)291112233"
