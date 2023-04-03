from django import forms
from .models import Candidate

class candidateformm(forms.ModelForm):
    
    class Meta:
        model = Candidate
        fields = "__all__"
 