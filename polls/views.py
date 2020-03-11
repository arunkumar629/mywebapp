from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
from polls.functions import handle_uploaded_file
from polls.forms import StudentForm



def index(request):
	if request.method=="POST":
		student=StudentForm(request.POST, request.FILES)
		if student.is_valid():
			handle_uploaded_file(request.FILES['file'])
			return HttpResponse("file uploaded successfully")
	else:
		student=StudentForm()
		return render(request, 'index.html', {'form':student})
