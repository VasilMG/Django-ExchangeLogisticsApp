from django.shortcuts import render

from ExchangeLogistics.common.models import ServicesData, NetworkData, AboutData

'''The below code which is marked as a comment is an exemplary code and can be used only if we add the same service types.
It should be used after we create a superuser and add some data to the common models.
I have divided the common information in 3 models , ServiceData, NetworkData, and AboutData.
If we add some information in them, then we can render their values to the templates.'''


def index(request):
    # user = request.user
    # road = ServicesData.objects.get(service_type='Road Transport Solutions')
    # sea = ServicesData.objects.get(service_type='Maritime Transport')
    # air = ServicesData.objects.get(service_type='Air Transport')
    # warehouse = ServicesData.objects.get(service_type='Warehouse Solutions')
    # fourpl = ServicesData.objects.get(service_type='4PL Solutions')
    # customs = ServicesData.objects.get(service_type='Customs Clearance Services')
    context = {
        # 'user': user,
        # 'road': road,
        # 'sea': sea,
        # 'air': air,
        # 'warehouse': warehouse,
        # 'fourpl': fourpl,
        # 'customs': customs,
    }
    return render(request, 'common/index.html', context)


def services(request):
    # all_services = ServicesData.objects.all()
    context = {
        # 'services': all_services,
    }
    return render(request, 'common/services_main.html', context)


def network(request):
    # offices = NetworkData.objects.all().order_by('country')
    context = {
        # 'offices': offices,
    }
    return render(request, 'common/network.html', context)


def about(request):
    # data = AboutData.objects.get(pk=1)
    context = {
        # 'data': data,
    }
    return render(request, 'common/about.html', context)
