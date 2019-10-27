from wtforms_alchemy import ModelForm
from .db_models import User, Group, Lecture


class UserForm(ModelForm):
    class Meta:
        model = User


class GroupForm(ModelForm):
    class Meta:
        model = Group


class LectureForm(ModelForm):
    class Meta:
        model = Lecture
