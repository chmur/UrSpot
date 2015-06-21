from django.shortcuts import render_to_response

from app1.models import spots

# Create your views here.
def home(request):
	entries = spots.objects.all()

	return render_to_response('index.html', {'spots' : entries})
