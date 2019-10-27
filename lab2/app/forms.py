from wtforms_alchemy import ModelForm
from .db_models import User


class UserForm(ModelForm):
    class Meta:
        model = User
