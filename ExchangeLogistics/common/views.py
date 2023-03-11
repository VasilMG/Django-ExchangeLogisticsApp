from django.shortcuts import render

from ExchangeLogistics.common.models import ServicesData, NetworkData, AboutData


def index(request):
    user = request.user
    ''' The below code should be added after we make a superuser and create the models for the ServicesData'''
    # road = ServicesData.objects.get(service_type='Road Transport Solutions')
    # sea = ServicesData.objects.get(service_type='Maritime Transport')
    # air = ServicesData.objects.get(service_type='Air Transport')
    # warehouse = ServicesData.objects.get(service_type='Warehouse Solutions')
    # fourpl = ServicesData.objects.get(service_type='4PL Solutions')
    # customs = ServicesData.objects.get(service_type='Customs Clearance Services')
    context = {
        'user': user,
        # 'road': road,
        # 'sea': sea,
        # 'air': air,
        # 'warehouse': warehouse,
        # 'fourpl': fourpl,
        # 'customs': customs,
    }

    return render(request, 'common/index.html', context)


def services(request):
    all_services = ServicesData.objects.all()
    context = {
        'services': all_services,
    }
    return render(request, 'common/services_main.html', context)


def network(request):
    offices = NetworkData.objects.all()
    context = {
        'offices': offices,
    }
    return render(request, 'common/network_new.html', context)


def about(request):
    ''' After we create a model for the AboutData'''
    # context = {
    #     'about_data': AboutData.objects.get(pk=1)
    # }
    return render(request, 'common/about.html') # Add contex here if you have created a model
