from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.utils import timezone
from app1.models import spots
from .forms import spotsForm


def spot_list(request):
	entries = spots.objects.all()[:10]

	return render_to_response('app1/spot_list.html', {'spots' : entries})

def spot_detail(request, pk):
    entries = get_object_or_404(spots, pk=pk)
    return render(request, 'app1/spot_detail.html', {'spots': entries})

#def spot_new(request):
#    form = spotsForm()
#    return render(request, 'app1/spot_edit.html', {'form': form})

def spot_new(request):
    if request.method == "POST":
        form = spotsForm(request.POST)
        if form.is_valid():
            spot = form.save(commit=False)
            spot.save()
            return redirect('app1.views.spot_list')
    else:
        form = spotsForm()
    return render(request, 'app1/spot_edit.html', {'form': form})


#def home(request):
#	entries = spots.objects.all()[:10]

#	return render_to_response('index.html', {'spots' : entries})

#def home1(request):
#	entries = spots.objects.all()[:10]

#	return render_to_response('index.html', {'spots' : entries})
