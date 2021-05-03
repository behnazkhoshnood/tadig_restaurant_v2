from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    max_delivery_fee = 60

    if delivery < max_delivery_fee:
        grand_total = total + delivery
    else:
        grand_total = total + max_delivery_fee

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'max_delivery_fee': max_delivery_fee,
        'grand_total': grand_total,
        
    }

    return context
