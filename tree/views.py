from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Tree


class TreeView(ListView):
    model = Tree
    template_name = "tree/base.html"

    

