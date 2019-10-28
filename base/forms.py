from django import forms
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import *

class DesignersForm(forms.Form):
	name = forms.CharField(max_length=255)

	def clean_name(self):
		if Designers.objects.filter(name = self.cleaned_data['name']).exists():
			raise ValidationError('Name is not Uniq')
		return self.cleaned_data['name']

	def save(self):
		newName = Designers.objects.create(name = self.cleaned_data['name'])
		return newName

class BuildersForm(forms.Form):
	name = forms.CharField(max_length=255)

	def clean_name(self):
		if Builders.objects.filter(name = self.cleaned_data['name']).exists():
			raise ValidationError('Name is not Uniq')
		return self.cleaned_data['name']

	def save(self):
		newName = Builders.objects.create(name = self.cleaned_data['name'])
		return newName

class FinishersForm(forms.Form):
	name = forms.CharField(max_length=255)

	def clean_name(self):
		if Finishers.objects.filter(name = self.cleaned_data['name']).exists():
			raise ValidationError('Name is not Uniq')
		return self.cleaned_data['name']

	def save(self):
		newName = Finishers.objects.create(name = self.cleaned_data['name'])
		return newName