from django.shortcuts import render, render_to_response, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from .models import Event, News, Quote, Album_Category, Album, Image
from django.template import RequestContext
#from .forms import ContactForm

def index(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')[:1]
    news = News.objects.order_by('-date')[:1]
    return render(request, 'pages/index.html', {'events': events, 'news': news})

def about(request):
    return render(request, 'pages/about.html', {})

def constitution(request):
    return render(request, 'pages/constitution.html', {})

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
    news = News.objects.order_by('-date')

    page = request.GET.get('page', 1)
    paginator = Paginator(news, 2)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    
    return render(request, 'pages/news.html', {'news': news})

def wus(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'pages/wus.html', {'events': events})

def quote(request):
    quotes = Quote.objects.order_by('-date')

    page = request.GET.get('page', 1)
    paginator = Paginator(quotes, 6)

    try:
        quotes = paginator.page(page)
    except PageNotAnInteger:
        quotes = paginator.page(1)
    except EmptyPage:
        quotes = paginator.page(paginator.num_pages)
        
    return render(request, 'pages/quote.html', {'quotes': quotes})

#def gallery(request):
#    albums = Album.objects.order_by('album_name')
        #return render(request, 'pages/gallery.html', {'albums': albums})
#    return render_to_response('pages/gallery.html', {'albums' : albums})

def album_categories(request):

    #albums = Album.objects.all
    album_categories = Album_Category.objects.all
    
    #return render(request, 'pages/gallery.html', {'albums': albums})
    return render(request, 'pages/album_categories.html', {'album_categories': album_categories})

def album_category(request, pk):
    #album_category = get_object_or_404(Album_Category, pk=pk)
    #album_category = Album_Category.objects.get(id=pk)
    #albums = Album_Category.objects.get(id=pk).album_set.all
    album_category = Album_Category.objects.get(id=pk)
    #albums = Album_Category.objects.all()
    return render(request, 'pages/albums.html', {'album_category': album_category})
    #return render(request, 'pages/albums.html', {'albums': albums})

#def committee(request):
#    return render(request, 'pages/committee.html', {})

def contact(request):
    #form_class = ContactForm

    #if request.method == 'POST':
    #    form = form_class(data=request.POST)

     #   if form.is_valid():
      #      contact_name = request.POST.get('contact_name', '')
      #      contact_email = request.POST.get('contact_email', '')
      #      form_content = request.POST.get('content', '')

    #        template = get_template('pages/contact_template.txt')
    #        context = {
    #            'contact_name': contact_name,
     #           'contact_email': contact_email,
   #             'form_content': form_content,
     #       }
     #       content = template.render(context)

      #      email = EmailMessage(
      #          "New contact form submission",
     #           content,
      #          "Your website" + '',
      #          ['youremail@gmail.com'],
      #          headers = {'Reply-To': contact_email }
     #       )

     #       email.send()
     #       return redirect('contact')
            
    #return render(request, 'pages/contact.html', {'form': form_class})
    return render(request, 'pages/contact.html', {})

def privacy_notice(request):
    return render(request, 'pages/privacy_notice.html', {})
