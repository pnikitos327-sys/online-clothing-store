from .models import Cart, CartItem

def get_cart(request):

    session_key = request.session.session_key

    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart, created = Cart.objects.get_or_create(session_key = session_key)
    return cart


def add_to_cart(request, product):
    cart = get_cart(request)
    cartItem, created = CartItem.objects.get_or_create( cart = cart, product = product, defaults = {'quantity' : 1})

    if not created:
        cartItem.quantity += 1

    cartItem.save()

    return cart



    