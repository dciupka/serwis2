from django.shortcuts import render, redirect
import requests
import json
from .forms import Size, SecondEndpointForms
from .models import Geoinfo
import csv
from django.http import HttpResponse


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
                objects = Geoinfo.objects.all()
                response = HttpResponse(content_type='text/csv')
                writer = csv.writer(response)
                writer.writerow(['type','_id','type','name','latitude', 'longtitude'])
                for ob in objects:
                    writer.writerow([ob._type, ob._id, ob.type, ob.name, ob.latitude, ob.longitude])
                response['Content-Disposition'] = 'attachment; filename="all_locations.csv"'
                return response
                #return redirect('api/json/all')
        else:
            form = Size()
            return render(request, 'serwis2/index.html', {'form': form,'form_2':form_2})

    return render(request, 'serwis2/index.html', {'form': 'form'})


def endpoint(request):
    if request.method == "POST":
        form = SecondEndpointForms(request.POST)
        if form.is_valid():
            field = form.cleaned_data['zapytanie']
            input_list =field.split(',')

            searching_list=[]
            for element in input_list:
                if element == 'id':
                    searching_list.append('_id')  # id without "_"
                else:
                    searching_list.append(element.strip())
            print(searching_list)
            data = Geoinfo.objects.all()
            print(data)
            response = HttpResponse(content_type='text/csv')
            writer = csv.writer(response)
            print_lista = []
            for i in data:
                for e in searching_list:
                    if e=='_id':
                        print_lista.append(i._id)
                    elif e=='latitude':
                        print_lista.append(i.latitude)
                    elif e== 'longitude':
                        print_lista.append(i.longitude)
                    elif e == 'type':
                        print_lista.append(i.type)
                    elif e == '_type':
                        print_lista.append(i._type)
                    elif e == 'name':
                        print_lista.append(i.name)
                writer.writerow(print_lista)
                print_lista.clear()
            response['Content-Disposition'] = 'attachment; filename="name.csv"'
            return response



    else:
        form = SecondEndpointForms()
    context = {'response': 'response', 'form':form}
    return render(request, 'serwis2/endpoint.html', context)



'''

def endpoint(request):
    if request.method == "POST":
        form = SecondEndpointForms(request.POST)
        if form.is_valid():
            id = form.cleaned_data['_id']
            lat= form.cleaned_data['latitude']
            lon= form.cleaned_data['longitude']
            print(f'{id}, {lon} xxxxx {lat}')
            data = Geoinfo.objects.all()
            print("___________________")
            for item in data:
                if item._id ==id and item.latitude==lat and item.longitude==lon:
                    obj = Geoinfo.objects.filter(_id = id)
                    context ={'obj':obj}
                    response = HttpResponse(content_type='text/csv')
                    lista = []
                    for ob in obj:
                        lista.append(ob._id)
                        lista.append(ob.latitude)
                        lista.append(ob.longitude)

                    print(lista)
                    writer = csv.writer(response)
                    writer.writerow(['id', 'latitude', 'longtitude'])
                    writer.writerow(lista)
                    response['Content-Disposition'] = 'attachment; filename="name.csv"'
                    return response

    else:
        form = SecondEndpointForms()
    context = {'response': 'response', 'form':form}
    return render(request, 'serwis2/endpoint.html', context)
def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    lista = []
    writer = csv.writer(response)
    writer.writerow(['id','latitude','longtitude'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    response['Content-Disposition']= 'attachment; filename="somefilename.csv"'
    return response



def endpoint(request):
    if request.method == "POST":
        form = SecondEndpointForms(request.POST)
        if form.is_valid():
            id = form.cleaned_data['_id']
            lat= form.cleaned_data['latitude']
            lon= form.cleaned_data['longitude']
            print(f'{id}, {lon} xxxxx {lat}')
            data = Geoinfo.objects.all()
            print("___________________")
            for item in data:
                if item._id ==id and item.latitude==lat and item.longitude==lon:
                    obj = Geoinfo.objects.filter(_id = id)
                    print(obj)

    else:
        form = SecondEndpointForms()
    context = {'response': 'response', 'form':form}
    return render(request, 'serwis2/endpoint.html', context)
'''