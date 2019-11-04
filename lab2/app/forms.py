from wtforms_alchemy import ModelForm
from .db_models import User, Group, Lecture, University


class UserForm(ModelForm):
    class Meta:
        model = User


class GroupForm(ModelForm):
    class Meta:
        model = Group


class LectureForm(ModelForm):
    class Meta:
        model = Lecture
        only = (
            'text',
            'version',
        )


class UniversityForm(ModelForm):
    class Meta:
        model = University
