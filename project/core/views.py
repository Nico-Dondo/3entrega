from django.shortcuts import render


def home(request):
    return render(request, "core/index.html")


def about(request):
    return render(request, "core/about.html")

def cliente(request):
    return render (request, "cliente/crear.html")
def obtener_resultados_segun_busqueda(query):
    # Lógica de búsqueda simple para coincidencia de subcadenas en nombres
    bateristas = [
        {"nombre": "Aquiles Priester", "imagen": "aquiles-priester-drums.jpg", "descripcion": "Descripción..."},
        {"nombre": "Lars Ulrich", "imagen": "descarga.jpg", "descripcion": "Descripción..."},
        {"nombre": "Ray Luzier", "imagen": "korn.jpg", "descripcion": "Descripción..."},
       
    ]

    resultados = [baterista for baterista in bateristas if query.lower() in baterista['nombre'].lower()]
    return resultados

def search(request):
    query = request.GET.get('q', '')
    results = obtener_resultados_segun_busqueda(query)
    return render(request, 'core/about.html', {'query': query, 'results': results})