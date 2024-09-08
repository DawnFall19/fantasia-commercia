from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306259950',
        'name': 'Michael Ignasius',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)