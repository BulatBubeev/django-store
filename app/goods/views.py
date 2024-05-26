from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render

from goods.models import Product


def catalog(request, category_slug):
    page = request.GET.get("page", 1)
    if category_slug == "all":
        goods = Product.objects.all()
    else:
        goods = get_list_or_404(Product, category__slug=category_slug)
    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)
    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {
        "product": product,
    }
    return render(
        request,
        "goods/product.html", context
    )
