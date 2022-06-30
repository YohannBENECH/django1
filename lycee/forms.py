from django import forms

from django.forms import ModelForm
from django.forms import BooleanField
from .models import Student, CallOfRoll


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'email',
            'phone',
            'comments',
            'cursus'
        ]


class CallOfRollForm(ModelForm):
    class Meta:
        model = CallOfRoll
        fields = [
            'dateOfCall',
            'isMissing',
            'reason',
            'student'
        ]


class CallOfRollSimpleForm(ModelForm):
    CheckBoxPresent = forms.BooleanField(label='')