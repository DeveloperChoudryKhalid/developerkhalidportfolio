from django.shortcuts import render
def KhalidPortfolio_view(request):
    return render(request, 'Home.html')
def About(request):
    return render(request, 'About.html')
def contact(request):
    return render(request, 'contact.html')
def credentials(request):
    return render(request, 'credentials.html')
def Home(request):
    return render(request, 'Home.html')
def MyOffering(request):
    return render(request, 'MyOffering.html')
def WorkDetails(request):   
    return render(request, 'WorkDetails.html')
def ProjectList(request):
    return render(request, 'ProjectList.html')
