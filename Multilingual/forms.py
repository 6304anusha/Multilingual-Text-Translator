from django import forms

class TextForm(forms.Form):
    input_text = forms.CharField(
        label="Enter Text",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Enter text in any language',
            'style': 'width:100%; font-size:1rem;'
        })
    )
