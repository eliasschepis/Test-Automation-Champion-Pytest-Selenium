import requests

# Test para comprobar que la respuesta del endpoint /users?page=2 es válida
def test_get_users_success(base_url):
    # Realizamos un GET a la API, en la ruta /users?page=2
    response = requests.get(f"{base_url}/users?page=2")

    # Validamos que el código de estado HTTP sea 200 (OK)
    assert response.status_code == 200

    # Convertimos la respuesta a JSON para poder acceder a sus campos
    json_data = response.json()

    # Verificamos que exista la clave "data" en la respuesta
    assert "data" in json_data

    # Verificamos que haya al menos un usuario dentro del array "data"
    assert len(json_data["data"]) > 0

    # Verificamos que cada usuario tenga un campo "email"
    for user in json_data["data"]:
        assert "email" in user



# Test POST

# Test para crear un nuevo usuario con POST
def test_create_user(base_url):
    # Definimos el cuerpo (payload) del request
    payload = {
        "name": "elias",
        "job": "qa engineer"
    }

    # Enviamos el request POST a /users con JSON en el cuerpo
    response = requests.post(f"{base_url}/users", json=payload)

    # Esperamos un código de respuesta 201 (CREATED)
    assert response.status_code == 201

    # Parseamos la respuesta a JSON
    json_data = response.json()

    # Validamos que los campos enviados estén en la respuesta
    assert json_data["name"] == "elias"
    assert json_data["job"] == "qa engineer"

    # Validamos que la respuesta incluya un ID generado
    assert "id" in json_data

    # Validamos que se haya generado una fecha de creación
    assert "createdAt" in json_data



# Test PUT

# Test para actualizar un usuario existente con PUT
def test_update_user(base_url):
    payload = {
        "name": "elias_updated",
        "job": "senior qa"
    }

    # Enviamos PUT al endpoint /users/2
    response = requests.put(f"{base_url}/users/2", json=payload)

    assert response.status_code == 200
    json_data = response.json()

    # Verificamos que los datos actualizados estén en la respuesta
    assert json_data["name"] == "elias_updated"
    assert json_data["job"] == "senior qa"
    assert "updatedAt" in json_data



# Test DELETE

# Test para eliminar un usuario (simulado en esta API)
def test_delete_user(base_url):
    # Enviamos DELETE al endpoint /users/2
    response = requests.delete(f"{base_url}/users/2")

    # La API devuelve 204 No Content si fue exitoso
    assert response.status_code == 204
