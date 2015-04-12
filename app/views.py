"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django import forms
from .forms import MyInput
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

# knapsack
def knapsack(request):
    """Renders the knapsack game page."""

    if request.method == 'POST':
        my_form = MyInput(request.POST or None)  # None means not entered

        if my_form.is_valid():
            my_data = my_form.cleaned_data['my_input']
            print my_data
            #print my_form
    else:
        form = MyInput()

    return render(request, 'app/knapsack.html',

                  context_instance = RequestContext(request,
                    {
                     'title':'Knapsack Problem',
                     'my_form': 'my_form',
                     'my_data': 'my_data',
                     })
                 )

def load_data():
    """ Loads the data from asterank and """



