import json
import os
from django.shortcuts import render

# Create your views here.

def index(request):
    json_path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(json_path, 'r') as file:
        sections = json.load(file)
    return render(request, 'index.html', {'sections': sections})
