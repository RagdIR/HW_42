from django.shortcuts import render

def index_view(request):
    total = 0
    if request.POST.get('check') == 'add':
        total = int(request.POST.get('number_1')) + int(request.POST.get('number_2'))

    elif request.POST.get('check') == 'substract':
        total = int(request.POST.get('number_1')) - int(request.POST.get('number_2'))


    elif request.POST.get('check') == 'multiply':
        total = int(request.POST.get('number_1')) * int(request.POST.get('number_2'))


    elif request.POST.get('check') == 'divide':
        total = int(request.POST.get('number_1')) / int(request.POST.get('number_2'))


    # return render(request, 'parts/total.html', {'result': total})


    return render(request, 'index.html',
                  {'number_1': request.POST.get('number_1'),
                   'check': request.POST.get('check'),
                   'number_2': request.POST.get('number_2'),
                   'result': total})