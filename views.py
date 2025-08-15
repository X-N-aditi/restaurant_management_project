from django.shortcuts import render

def menu_lists(request):
    menu_items = {
        {
            "name": "Red Sauce Pasta",
            "price": 300,
            "description": "Red tomato pasta with rosemary-leaf"
        }
        {
            "name": "Margherita Pizza",
            "price": 400,
            "description": "Cheeze pizza with basil-leaf"
        }
    }
    return render(request, 'menu_list.html', {"menu_items": menu_items})