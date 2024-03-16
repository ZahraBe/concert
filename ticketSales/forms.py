from django import forms
from ticketSales.models import concertModel
from ticketSales.models import ticketModel

class SearchForm(forms.Form):
    SearchText=forms.CharField(max_length=100, label="نام کنسرت یا خواننده", required=False)

class ConcertForm(forms.ModelForm):
    class Meta:
        model= concertModel
        fields=['Name','SingerName','length', 'Poster']
        # exclude=["Poster"]

class TicketForm(forms.ModelForm):
    class Meta:
        model= ticketModel
        fields=['timeModel']
    name=forms.CharField(max_length=100, label="نام و نام خانوادگی", required=True)
    code=forms.CharField(max_length=10,label="کد ملی", required=True)