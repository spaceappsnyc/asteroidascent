"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django import forms
from .forms import CostInput
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

    cost_form = CostInput(request.GET or None)  # None means not entered
    if cost_form.is_valid():
        cost = cost_form.cleaned_data['cost']
        print cost

    return render(request, 'app/knapsack.html',

                  context_instance = RequestContext(request,
                    {
                     'title':'Knapsack Problem',
                     'cost':'cost',
                     'cost_form': 'cost_form'
                     })
                 )
    #return render_to_response("knapsack.html",
    #                          locals(),
    #                          context_instance=RequestContext(request)
    #                          )