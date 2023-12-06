from django import forms

class DjangoForm(forms.Form) :
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    agree = forms.BooleanField()
    salary = forms.IntegerField()
    expence = forms.FloatField(required=False)
    date = forms.DateField()
    value = forms.DecimalField()
    description = forms.TextInput()
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    CHOICES = [('blue', 'Blue'),('green', 'Green'), ('black', 'Black'),]
    favorite_color = forms.ChoiceField(choices=CHOICES)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=CHOICES)
    image = forms.FileField(required=False)
    comment1 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    comment2 = forms.CharField(widget=forms.Textarea, max_length=200)