from django.test import TestCase
from django.shortcuts import render, redirect
import requests
import json
from .forms import Size
from .models import Geoinfo


def index(request):
    if request.method == 'POST':
        form = Size(request.POST)
        if form.is_valid():
            data = requests.get(f'https://serwis01.herokuapp.com/generate/json/all/')
            response = data.json()
            if len(response) > 0:
                data_in_databse = Geoinfo.objects.all()
                id_list = []
                for id in data_in_databse:
                    id_list.append(id._id)
                print(id_list)
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
                            id_list.append(dictionary_data['_id']) #gdy pusto
                            print(f"Zapisano do bazy {dictionary_data['name']}")
                            continue
                        else:
                            print(f"{dictionary_data['_id']}- jest już na liscie")
                    break
                return redirect('api/json/all')
            else:
                form = Size()
            return render(request, 'serwis2/index.html', {'form': form})

    return render(request, 'serwis2/index.html', {'form': 'form'})


def endpoint(request):
    context = {'response': 'response'}
    return render(request, 'serwis2/endpoint.html', context)
