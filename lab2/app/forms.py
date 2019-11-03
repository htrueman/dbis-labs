from wtforms import Form
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import Required, DataRequired
from wtforms_alchemy import ModelForm
from .db_models import User, Group, Lecture


class UserForm(ModelForm):
    class Meta:
        model = User


class GroupForm(Form):
    class Meta:
        model = Group
        include_primary_keys = True


class LectureForm(ModelForm):
    # created = DateTimeLocalField(format='%d/%m/%y %h:%mm', validators=[DataRequired()])
    # modified = DateTimeLocalField(format='%d/%m/%y %h:%mm', validators=[DataRequired()])

    class Meta:
        model = Lecture
        only = (
            'text',
            'version',
        )
