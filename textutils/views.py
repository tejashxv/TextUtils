from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    para = {"name":"tejash yadav","state":"Utttar preadesh"}
    return render(request, 'index2.html',para)

def analyze(request):
    
    djtext = request.POST.get('text', 'default')
    punc = request.POST.get('removepunc', 'off')
    upperc = request.POST.get('upper', 'off')
    lineremover = request.POST.get('lineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounts = request.POST.get('charcounts', 'off')
    
   
    punctuation_marks = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    analyzed = djtext  
    
    
    if punc == "on":
        analyzed = "".join(char for char in analyzed if char not in punctuation_marks)
        return render(request, 'analyze.html', {"purpose": "Text Analysis", "analyzed_text": analyzed})

    
    elif upperc == "on":
        analyzed = analyzed.upper()
        return render(request, 'analyze.html', {"purpose": "Text Analysis", "analyzed_text": analyzed})

   
    elif lineremover == "on":
        analyzed = "".join(char for char in analyzed if char != "\n" and char != "\r")
        return render(request, 'analyze.html', {"purpose": "Text Analysis", "analyzed_text": analyzed})

    
    elif spaceremover == "on":
        analyzed = " ".join(analyzed.split())
        return render(request, 'analyze.html', {"purpose": "Text Analysis", "analyzed_text": analyzed})
    
   
    elif charcounts == "on":
        char_count = len(analyzed.replace(" ", ""))
        return render(request, 'analyze.html', {"purpose": "Character Count", "analyzed_text": f"Character count: {char_count}"})
    
   
    else: 
        return HttpResponse("Error: No operation selected.")
    


        
    
            

   
