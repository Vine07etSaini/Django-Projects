#I Have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
        return render(request,'index.html')
def analyze(request):
        #Get the text
        djtext=request.POST.get('text','defualt')
        removepunc=request.POST.get('removepunc','off')
        capfirst=request.POST.get('capfirst','off')
        remspace=request.POST.get('remspace','off')
        newlineremove=request.POST.get('newline','off')
        # Analyze the Text 
        if removepunc=="on":
            analyzed=""
            punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            for char in djtext:
                if char not in punctuations:
                        analyzed+=char
            djtext=analyzed
            params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
     
        if removepunc=="on":
            analyzed=""
            punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            for char in djtext:
                if char not in punctuations:
                        analyzed+=char
            djtext=analyzed
             
            params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        
        if capfirst=="on":
            analyzed=djtext.upper()
            djtext=analyzed
            params={'purpose':'Capital Letters','analyzed_text':analyzed}

        if newlineremove=="on":
             analyzed=" ".join(djtext.splitlines())
             djtext=analyzed
            
             params={'purpose':'Removed newLine','analyzed_text':analyzed}
        
        if remspace=="on":
            analyzed=""
            for index,char in enumerate(djtext):
                if djtext[index] ==" " and djtext[index+1]==" ":
                        pass
                else:
                    analyzed+=char
            djtext=analyzed
              
            params={'purpose':'Removed Space','analyzed_text':analyzed}

        if remspace!="on" and newlineremove!="on" and capfirst!="on" and  removepunc!="on" :
                    return HttpResponse("Error")
        

        return render(request,'analyze.html',params)
         
       