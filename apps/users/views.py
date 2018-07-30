from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'index.html', {})

