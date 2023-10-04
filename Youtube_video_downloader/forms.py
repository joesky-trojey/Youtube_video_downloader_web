from django import forms


class linkForm(forms.Form):
    link=forms.CharField(max_length=100, required=True, widget=forms.URLInput(attrs={'class':'form-control'}))
    format=forms.ChoiceField(choices=[('mp4','Mp4'),('mp3','Mp3')], widget=forms.Select(attrs={'class':'form-control', 'id':'sel1'}))
    quality=forms.ChoiceField(choices=[('high','high'),('medium','medium'), ('low','low')], widget=forms.Select(attrs={'class':'form-control', 'id':'sel1'}))
