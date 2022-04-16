from django.test import TestCase
from django.shortcuts import render, redirect
import requests
import json
from .forms import Size
from . models import Geoinfo


def index(request):
    if request.method != 'POST':
        form=Size()
    else:
        form = Size(data=request.POST)
    if form.is_valid():
        data = requests.get(f'https://serwis01.herokuapp.com/generate/json/all/')
        response = data.json()

        data_in_databse=Geoinfo.objects.all()
        id_list=[]
        for id in data_in_databse:
            id_list.append(id._id)

        while True:
            for dictionary_data in response:
                if dictionary_data['_id'] not in id_list:
                    item = Geoinfo(_type=dictionary_data['_type'],
                                   _id=dictionary_data['_id'],
                                   name=dictionary_data['name'],
                                   type=dictionary_data['type'],
                                   latitude=dictionary_data['geo_position']['latitude'],
                                   longitude=dictionary_data['geo_position']['longitude']
                                   )
                    item.save()
                    print(f"Zapisano do bazy {dictionary_data['name']}")
                    continue
                elif dictionary_data['_id'] in id_list:
                    print(f"{dictionary_data['_id']} to id jest juz w bazie")
                    continue
                else:
                    print('Wszystkie zapisano')
                    break
        return redirect('api/json/all')
    context = {'response': 'response', 'form':form}
    return render(request, 'serwis2/index.html', context)


def endpoint(request):
    context = {'response': 'response'}
    return render(request, 'serwis2/endpoint.html', context)

elif dictionary_data['_id'] in id_list:
print(f"{dictionary_data['_id']} to id jest juz w bazie")