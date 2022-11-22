from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Field
from django.core.exceptions import ValidationError
class DateForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(Field('date'), css_class='col-md-4'),
                Div(Field('date2'), css_class='col-md-4'),
                Div(Submit('submit', '送出', css_class='mt-4 w-100'), css_class='col-md-2'),
            css_class='row'),
        )
        self.error_messages = {
            'date_mismatch': ('結束日只能選開始日或是開始日後，請重新查詢結束日期'),
        }
    date = forms.DateTimeField(
        label = ("欲顯示開始日期，僅顯示選擇開始日"),
        input_formats=['%Y/%m/%d'],
        widget=forms.DateTimeInput(attrs={
            'id': 'datepicker',
            'class': 'col-md-6 form-control datetimepicker-input',
            'data-target': '#datetimepicker1',
            'autocomplete': 'off'
        })
    )

    date2 = forms.DateTimeField(
        required= False,
        label = ("欲顯示結束日期，僅顯示選擇結束日"),
        input_formats=['%Y/%m/%d'],
        widget=forms.DateTimeInput(attrs={
            'id': 'datepicker2',
            'class': 'col-md-6 form-control datetimepicker-input',
            'data-target': '#datetimepicker2',
            'autocomplete': 'off'
        })
    )
    def clean_date2(self):
        date = self.cleaned_data.get("date")
        date2 = self.cleaned_data.get("date2")
        
        if date and date2 and date > date2:
            raise ValidationError(
                self.error_messages['date_mismatch'],
                code = 'date_mismatch',
            )
        return date2