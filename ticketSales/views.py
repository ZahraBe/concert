from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from ticketSales.models import concertModel
from ticketSales.models import locationModel
from ticketSales.models import timeModel 
from django.urls import reverse
import ticketSales
import accounts
from django.contrib.auth.decorators import login_required
from ticketSales.forms import SearchForm, ConcertForm, TicketForm


# Create your views here.
def concertListView(request):

    searchForm=SearchForm(request.GET)
    if searchForm.is_valid():
        SearchText=searchForm.cleaned_data["SearchText"]
        concerts=concertModel.objects.filter(Name__contains=SearchText)
        concerts=concertModel.objects.filter(SingerName__contains=SearchText)


    else:
        concerts=concertModel.objects.all()

    context={
        "concertlist" : concerts,
        "concertcount" : concerts.count(),
        "searchForm" :searchForm
    }

    return render(request,"ticketSales/concertlist.html", context)

@login_required
def locationListView(request):
    locations=locationModel.objects.all()

    context={
        "location" : locations,
    }

    return render(request,"ticketSales/locationlist.html", context)

def concertDetailsView(request, concert_id):
    concert= concertModel.objects.get(pk=concert_id)

    context={
        "concertdetails": concert
    }
    return render(request,"ticketSales/concertDetails.html", context) 

@login_required
def timeView(request):   
    # if request.user.is_authenticated and request.user.is_active:
        times=timeModel.objects.all()

        context={
            "timelist": times,
        }
        return render(request,"ticketSales/timeList.html", context)
    # else:
        # return HttpResponseRedirect(reverse(accounts.views.loginView))

@login_required
def concertEditView(request, concert_id):
    concert= concertModel.objects.get(pk=concert_id)

    if request.method== "POST":
        concertForm=ConcertForm(request.POST, request.FILES, instance=concert)
        if concertForm.is_valid:
            concertForm.save()
            return HttpResponseRedirect(reverse(ticketSales.views.concertListView))
 
    else:
        concertForm=ConcertForm(instance=concert)

    context={
         "concertForm": concertForm,
         "PosterImage": concert.Poster
    }

    return render(request,"ticketSales/concertEdit.html", context)
    


def sell_ticket_view(request):
    if request.method=='POST':
        form = TicketForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('payment_url')
    else:
        form = TicketForm()
        return render(request,'ticketSales/sell_ticket.html', {'form': form})