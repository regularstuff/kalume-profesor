from django import forms

class CreateEnergyForm(forms.Form):
    
    planets = forms.IntegerField(
        max_value=100,
        min_value=0,
        required=True,
        initial=1,
        label='Number of planets',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Planet Count'})
    )
    fusion = forms.IntegerField(
        max_value=100,
        min_value=0,
        required=True,
        initial=0,
        label='Fusion Level',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Fusion Level'})
    )
    energy = forms.IntegerField(
        max_value=100,
        min_value=0,
        required=True,
        initial=0,
        label='Energy Level',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Energy Level'})
    )
    commander = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    engineer = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
    life_form_type = forms.ChoiceField(
        choices={'0': 'Choose your life-form','1':'Humans','2':'Rocktal','3':'Kaelesh','4':'Mechas'},
        required=False,
        initial='0',
        label='Choose your life-form',
        label_suffix=':',
        widget=forms.Select(attrs={'class': 'form-select'}),
        

    )
    life_form_level = forms.IntegerField(
        max_value=100,
        min_value=0,
        required=False,
        label='Life Form Level',
        initial='Life Form Level',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Life Form Level'})
    )
    steps = forms.IntegerField(
        max_value=1000,
        min_value=1,
        required=True,
        label='Desired Steps',
        initial='Desired Steps',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Desired Steps'})
    )