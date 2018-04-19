from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Event

def index(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')#[:3]
    return render(request, 'pages/index.html', {'events': events})

def about(request):
    return render(request, 'pages/about.html', {})

def events(request):
    #events = Event.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #events = Event.objects.order_by('-date')[:3]
    #events = Event.objects.order_by('date')
    event_list = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    #page = request.GET.get('page', 1)
    #paginator = Paginator(event_list, 6)

    #try:
    #    events = paginator.page(page)
    #except PageNotAnInteger:
    #    events = paginator.page(1)
    #except EmptyPage:
    #    events = paginator.page(paginator.num_pages)
    
    #return render(request, 'pages/events.html', {'events': events})
    #return render(request, 'pages/events.html', {'events': events})
    return render(request, 'pages/events.html', {'events': event_list})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'pages/event_detail.html', {'event': event})

def news(request):
    return render(request, 'pages/news.html', {})

def wus(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'pages/wus.html', {'events': events})

def quote(request):
    return render(request, 'pages/quote.html', {})

def gallery(request):
    return render(request, 'pages/gallery.html', {})

def committee(request):
    return render(request, 'pages/committee.html', {})

def contact(request):
    return render(request, 'pages/contact.html', {})
