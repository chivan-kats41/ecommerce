from django.urls import path
from . import views

urlpatterns = [
    path("faq/", views.faq, name="faq"),
    path("shipping/", views.shipping, name="shipping"),
    path("returns/", views.returns, name="returns"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
]