from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import Add
from .models import Serra

# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")


"""
@login_required
def dashboard(request):
    user_serra_objects = request.user.serra.all()
    serra_codex = [serra.code for serra in user_serra_objects]

    # Fill the list with empty strings to ensure it has 10 elements
    serra_codes = serra_codex + [""] * (10 - len(serra_codex))

    # Print the codes (for debugging purposes)
    print(serra_codes)
    
    return render(request, "dashboardMulti.html", {"serra_codes": serra_codes})
"""

@login_required
def dashboard_view(request, var=None):
    # Handle the variable 'var' here
    context = {'var': var , 'is_specific_serra': bool(var)  }
    return render(request, 'dashboard.html', context)

@login_required
def dashboard(request):

    

    #X70odAJONACz86q40l7MdtfauLgpPMga39oao-_ImlcKUKzV7uLyqhQXdSr6cuWqhbLilpv2pniPPuo46PadAA==
    user_serra_objects = request.user.serra.all()


    serra_codex = [serra.code for serra in user_serra_objects]

    serra_codes=["","","","","","","","","",""]

    # Extract the code attribute from each Serra object
    for i in range(10):
        try:
            serra_codes[i]=serra_codex[i]
        except:
            serra_codes[i]=""


    # Print the codes (for debugging purposes)
    print(serra_codes)
    
    return render(request,"dashboard.html", {"var" : serra_codes[0],"var1" : serra_codes[1],"var2" : serra_codes[2],
                                             "var3" : serra_codes[3],"var4" : serra_codes[4],"var5" : serra_codes[5],
                                               "var6" : serra_codes[6],"var7" : serra_codes[7],"var8" : serra_codes[8],"var9" : serra_codes[9]})
@login_required
def serre(request):

    return render(request, "serre.html")


