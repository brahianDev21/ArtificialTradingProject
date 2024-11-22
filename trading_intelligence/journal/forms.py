from django import forms
from django.core.validators import FileExtensionValidator
from .models import Journal
from crispy_forms.helper import FormHelper

class JournalForm(forms.ModelForm):

    class Meta:
        model = Journal
        fields = ['is_profit', 'title', 'content', 'img_filename', 'pair', 'order_type', 'lots', 'open_datetime',
                  'close_datetime', 'open_price', 'close_price', 'take_profit', 'stop_loss', 'commission']
        widgets = {
            
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'spellcheck': 'true', 'style': 'height:100px'}),
            'img_filename': forms.FileInput(attrs={'class': 'form-control'}),
            'is_profit': forms.Select(attrs={'class': 'form-select'}),
            'pair': forms.Select(attrs={'class': 'form-select'}),
            'order_type': forms.Select(attrs={'class': 'form-select'}),
            'lots': forms.NumberInput(attrs={'class': 'form-control'}),
            'open_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'close_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'open_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'close_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'take_profit': forms.NumberInput(attrs={'class': 'form-control'}),
            'stop_loss': forms.NumberInput(attrs={'class': 'form-control'}),
            'commission': forms.NumberInput(attrs={'class': 'form-control'})

        }
    
    def __init__(self, *args, **kwargs):
        super(JournalForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
        self.helper.include_media = False  # No incluir asteriscos automáticamente


    is_profit = forms.ChoiceField(choices=[
        (None, 'None'), 
        (True, 'True'), 
        (False, 'False')
    ], required=False)
    pair = forms.ChoiceField(choices=[
        ('eurusd', 'EUR/USD'),
        ('usdcad', 'USD/CAD'),
        ('gbpusd', 'GBP/USD'),
    ])
    order_type = forms.ChoiceField(choices=[
        ('buy', 'Buy'),
        ('sell', 'Sell')
    ])
    open_datetime = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])
    close_datetime = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])

    def clean_is_profit(self):
        value = self.cleaned_data.get('is_profit')
        if value == 'true':
            return True
        elif value == 'false':
            return False
        return None