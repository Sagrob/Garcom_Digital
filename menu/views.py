from django.shortcuts import render, redirect
from .models import Item, StockMovement
from .forms import StockMovementForm

def item_list(request):
    items = Item.objects.all()
    return render(request, 'inventory/item_list.html', {'items': items})

def stock_movement(request):
    if request.method == 'POST':
        form = StockMovementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = StockMovementForm()
    return render(request, 'inventory/stock_movement.html', {'form': form})
