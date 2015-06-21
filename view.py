from django.shortcuts import render_to_response

from APPNAME.models import spots


# Create your views here.
def home(request):
	return render_to_response('index.html')
