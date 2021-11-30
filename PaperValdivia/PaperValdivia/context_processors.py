import requests

ipCategory = 'http://localhost:8001'

def add_categories_to_context(request):
    categories = requests.get(ipCategory+'/categorias').json()
    return {
        'categorias': categories
    }