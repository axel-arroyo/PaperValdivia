import requests

ipCategory = 'http://localhost:8001'

def add_categories_to_context(request):
    try:
        categories = requests.get(ipCategory+'/categorias').json()
        return {
            'categorias': categories
        }
    except:
        return {}
        
    