from django import forms

from .models import spots

class spotsForm(forms.ModelForm):

    class Meta:
        model = spots
        fields = ('spotname', 'authorname', 'link', 'description', 'timestamp', 'tags')
