"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django import forms
from .forms import MyInput
from datetime import datetime
import pandas as pd

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

def asteroid_data(request):
    """Renders the asteroid data page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/asteroid_data.html',
        context_instance = RequestContext(request,
        {
            'title':'Asteroid Data Page',
            'year':datetime.now().year,
        })
    )


def nasa_arm(request):
    """Renders the nasa_arm page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/nasa_arm.html',
        context_instance = RequestContext(request,
        {
            'title':'Nasa Arm Page',
            'year':datetime.now().year,
        })
    )


def educate(request):
    """Renders the nasa_arm page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/nasa_arm.html',
        context_instance = RequestContext(request,
        {
            'title':'Educate Page',
            'year':datetime.now().year,
        })
    )




# knapsack
def knapsack(request):
    """Renders the knapsack game page."""

    items = []
    bagged= []
    if request.method == 'POST':
        my_form = MyInput(request.POST or None)  # None means not entered

        if my_form.is_valid():
            my_data = my_form.cleaned_data['my_input']
            print my_data
            print type(my_data)
            #print my_form


            items = load_data()
            # print type(items)
            # print items[0]
            #print items

            '''
            try:
                xrange
            except:
                xrange = range
            '''
            bagged = knapsack01_dp(items, my_data)
            print("Bagged the following items\n  " +
                  '\n  '.join(sorted(item for item,_,_ in bagged)))
            val, wt = totalvalue(bagged, my_data)
            print("for a total value of %i and a total weight of %i" % (val, -wt))

            print type(bagged)
            print bagged


    else:
        pass
        #form = MyInput()


    return render(request, 'app/knapsack.html',

                  context_instance = RequestContext(request,
                    {
                     'title':'Knapsack Problem',
                     'my_form': 'my_form',
                     #'items': [item[0] for item in items if item],
                     'items': items,
                     'bagged': bagged,
                     'my_data': 'my_data',
                     })
                 )


def load_data():
    """ Loads the data from asterank and """
    raw_data = pd.io.json.read_json('https://williamqliu.s3.amazonaws.com/space/asteroid_list_all.json')
    raw_data = raw_data[raw_data['price']>1]

    closeness = raw_data['closeness'].astype('int').tolist()
    price = raw_data['price'].astype('int').tolist()
    name = raw_data['full_name'].tolist()
    items = tuple(zip(name, closeness, price))
    return items


def totalvalue(comb, my_data):
    ' Totalise a particular combination of items'
    totwt = totval = 0
    for item, wt, val in comb:
        totwt  += wt
        totval += val
    return (totval, -totwt) if totwt <= my_data else (0, 0)


def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]

    for j in xrange(1, len(items) + 1):
        item, wt, val = items[j-1]
        for w in xrange(1, limit + 1):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j-1][w]

        if was_added:
            item, wt, val = items[j-1]
            result.append(items[j-1])
            w -= wt

    return result

