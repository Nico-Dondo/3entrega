from django.shortcuts import render
from django.shortcuts import render, redirect


def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def cliente(request):
    return render(request, "cliente/crear.html")



def buscar_view(request):
    query = request.GET.get('q', '')
    borrar_resultados = 'borrar' in request.GET

    if borrar_resultados:
        # Lógica para borrar todos los resultados almacenados en la sesión
        if 'resultados' in request.session:
            del request.session['resultados']
        return redirect('core:index')  # Cambia 'index' por el nombre de la URL de la página principal

    # Lógica de búsqueda aquí (puedes personalizar según tus necesidades)
    results = obtener_resultados_segun_busqueda(query)

    # Si estás volviendo a base.html, borra los resultados antiguos
    if 'resultados' in request.session:
        del request.session['resultados']

    # Almacena los resultados en la sesión para que estén disponibles en otras vistas
    request.session['resultados'] = results

    # Redirige a la página base.html
    return render(request, 'core/base.html', {'query': query, 'results': results})

def obtener_resultados_segun_busqueda(query):
    bateristas = [
        {"nombre": "Aquiles Priester", "imagen": 'core/img/aquiles-priester-drums.jpg', "descripcion": "Aquiles Priester (n. Otjo, Sudáfrica, 25 de junio de 1971) es un músico brasileño, baterista de las bandas de power metal Hangar y Primal Fear. En 2006 participó en el proyecto de Fábio Laguna, «Freakeys», y hasta 2008 fue el baterista de Angra."},
        {"nombre": "Lars Ulrich", "imagen": 'core/img/descarga.jpg', "descripcion": "Nació el 26 de diciembre de 1963 en Gentofte (Dinamarca), en el seno de una familia de clase media-alta. Siendo un prodigio del tenis en su juventud, Ulrich se trasladó a Los Ángeles, California, a la edad de dieciséis años para seguir con su educación, pero en vez de seguir jugando al tenis, decidió dedicarse a la batería. Después de publicar un anuncio en un periódico local de Los Ángeles, The Recycler, conoció a James Hetfield."},
        {"nombre": "Ray Luzier", "imagen": 'core/img/korn.jpg', "descripcion": 'Raymond Lee "Ray" Luzier (Pittsburgh, Pensilvania, 14 de junio de 1970) es un baterista de rock estadounidense. Es más conocido por haber formado parte de la banda Army of Anyone, un conjunto de rock compuesto por Richard Patrick y los hermanos Dean DeLeo y Robert DeLeo de Stone Temple Pilots. Actualmente es el baterista de la banda Korn y KXM.'},
    ]

    resultados = [baterista for baterista in bateristas if query.lower() in baterista['nombre'].lower()]
    return resultados
