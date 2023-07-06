from django import forms


class PostCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField()
