from .models import Cart, CartItems
from .views import _cart_id
from django.core.exceptions import ObjectDoesNotExist


def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            car_item = CartItems.objects.all().filter(cart=cart[:1])
            for cart_item in car_item:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)
