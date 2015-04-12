from django.shortcuts import render

# Create your views here.
def index(request):
	context_dict = {'name': 'Susan'}
	return render(request, "index.html", context_dict)