from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Category
from .forms import ItemForm, CategoryForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
def home(request):
    return render(request, 'home.html')
# CRUD for Item

def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'items/item_form.html', {'form': form})


def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'items/item_detail.html', {'item': item})


def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_detail', item_id=item.id)
    else:
        form = ItemForm(instance=item)
    return render(request, 'items/item_form.html', {'form': form, 'item': item})


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'items/item_confirm_delete.html', {'item': item})


# CRUD for Category

def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'categories/category_detail.html', {'category': category})


def update_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form, 'category': category})


def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        category.delete()
        return redirect('category_list')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})
def test(request):
    categories = Category.objects.all()
    items = Item.objects.all()
    return render(request,'index.html',{'items': items, 'categories': categories})


from django.core.serializers import serialize

def filter_items_by_category(request):
    category_id = request.GET.get('category_id')
    if not category_id:
        return JsonResponse({'error': 'Category ID is required'}, status=400)

    try:
        # Filter items based on category ID
        items = Item.objects.filter(category_id=category_id)
        category = Category.objects.get(id=category_id)  # Get the category

        if not items:
            return JsonResponse({'error': 'No items found for this category'}, status=404)

        # Serialize category data to avoid the JSON serialization error
        category_data = {
            'id': category.id,
            'title': category.title,
        }

        # Render the filtered items with category title
        html = render_to_string('menu_items.html', {'items': items, 'category': category})

        return JsonResponse({'html': html, 'category': category_data})

    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'Server Error: {str(e)}'}, status=500)
