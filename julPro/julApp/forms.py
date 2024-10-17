from django import forms


class DomCalculatorForm(forms.Form):
    suburb = forms.CharField(label="Suburb", max_length=100)
    property_type = forms.ChoiceField(
        choices=[("House", "House"), ("Apartment", "Apartment")]
    )
    price = forms.FloatField(label="Price")
