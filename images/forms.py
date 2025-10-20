from django import forms

FILTER_CHOICES = [
    ("gray", "Grayscale"),
    ("sepia", "Sepia"),
    ("blur", "Blur"),
    ("edge", "Edge"),
    ("poster", "Posterize"),
    ("solar", "Solarize"),
]

class UploadForm(forms.Form):
    image = forms.ImageField()
    filter_name = forms.ChoiceField(choices=FILTER_CHOICES)