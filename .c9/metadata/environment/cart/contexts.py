{"filter":false,"title":"contexts.py","tooltip":"/cart/contexts.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":21,"column":85},"action":"insert","lines":["from django.shortcuts import get_object_or_404","from products.models import Product","","","def cart_contents(request):","    \"\"\"","    Ensures that the cart contents are available when rendering","    every page","    \"\"\"","    cart = request.session.get('cart', {})","","    cart_items = []","    total = 0","    product_count = 0","    ","    for id, quantity in cart.items():","        product = get_object_or_404(Product, pk=id)","        total += quantity * product.price","        product_count += quantity","        cart_items.append({'id': id, 'quantity': quantity, 'product': product})","    ","    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":21,"column":85},"end":{"row":21,"column":85},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":26,"mode":"ace/mode/python"}},"timestamp":1565102119474,"hash":"9bb4d06b46bac6d09a11dfd6a48fe7ad7ca08766"}