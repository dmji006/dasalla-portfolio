from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Item


@api_view(["GET"])
def get_items(request):
    search_query = request.GET.get("search", "")
    if search_query:
        items = Item.objects.filter(name__icontains=search_query)
    else:
        items = Item.objects.all()

    data = list(items.values())
    return Response({"items": data})


@api_view(["GET"])
def get_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return Response(
        {
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "price": str(item.price),
        }
    )


@api_view(["POST"])
def add_item(request):
    data = request.data
    item = Item.objects.create(
        name=data["name"], description=data["description"], price=data["price"]
    )
    return Response({"message": "Item added", "item_id": item.id}, status=201)


@api_view(["PUT"])
def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    data = request.data
    item.name = data.get("name", item.name)
    item.description = data.get("description", item.description)
    item.price = data.get("price", item.price)
    item.save()
    return Response({"message": "Item updated"})


@api_view(["DELETE"])
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return Response({"message": "Item deleted"})
