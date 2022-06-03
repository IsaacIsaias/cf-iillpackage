import requests

def unreleased():
    """
        Realizar la petición y retornar el objeto JSON.
    """
    response = requests.get('https://codigofacilito.com/api/v2/workshops/unreleased') # Consumir un API
    
    if response.status_code == 200:
        payload = response.json() # Convertir lo retornado en un diccionario
        return payload['data'] # En 'data' existe el listado de workshops
