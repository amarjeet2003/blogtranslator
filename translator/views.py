from django.shortcuts import render
from . import translate
from googletrans import LANGUAGES

# Create your views here.

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        output = translate.translate(original_text, request.POST.get("language"))
        return render(request,'translator.html', {'output_text':output, 'original_text':original_text, "available_langs":LANGUAGES})

    else:
        return render(request,'translator.html', {"available_langs":LANGUAGES})
