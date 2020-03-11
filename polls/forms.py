from django import forms
class StudentForm(forms.Form):
	name=forms.CharField(label="Enter your name", max_length=50)
	file=forms.FileField()
