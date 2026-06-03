from django.shortcuts import render

def faq(request):
    return render(request, "pages/faq.html")

def shipping(request):
    return render(request, "pages/shipping.html")

def returns(request):
    return render(request, "pages/returns.html")

def privacy(request):
    return render(request, "pages/privacy.html")

def terms(request):
    return render(request, "pages/terms.html")