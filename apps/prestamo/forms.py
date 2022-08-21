from django import forms


class PrestamoForm(forms.Form):
    loan_type = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control mb-1'}),label='Tipo',choices=(('Personal','Prestamo personal'),('Prendario','Prestamo prendario'),('Hipotecario´','Prestamo hipotecario')),required=True)
    loan_date = forms.DateField(required= True, input_formats=['%Y-%m-%d'], label='Fecha de inicio',widget=forms.DateInput(attrs={'type':'date','class':'form-control mb-2'}))
    loan_total = forms.DecimalField(label='Monto', min_value=100, required=True,widget=forms.NumberInput(attrs={'class':'form-control mb-2 '}))