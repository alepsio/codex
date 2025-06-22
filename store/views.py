from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product, Order, SupportTicket


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})

@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    tickets = SupportTicket.objects.filter(user=request.user)
    return render(request, 'store/profile.html', {'orders': orders, 'tickets': tickets})
