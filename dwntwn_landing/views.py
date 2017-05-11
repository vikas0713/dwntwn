# __author__ = 'joyage'
"""
This file was generated on  machine.Joyage Online Solutions. Copyright 2015 
:purpose: 
:related to server:
:extra info
"""
from django.shortcuts import render


def index(request):
    """
    The index page of landing page
    :param request:
    :return:
    """
    return render(
        request,
        "index.html",
        {}
    )


