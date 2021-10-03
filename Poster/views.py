from django.shortcuts import render, redirect
from .forms import GenerateForm
from django.views.decorators.http import require_POST
from .Scraper import Scrape

def Home(request) :

    Quote          = Scrape()

    form           = GenerateForm()
    context = {
               'Quote'     : Quote,
               'Form'      : form,
               }

    return render(request,'Poster/home.html', context)

@require_POST
def GenerateItem(request):

    # form = GenerateForm(request.POST)
    # if form.is_valid():
    #     print(request.POST['Text'])
    return redirect('Home')
