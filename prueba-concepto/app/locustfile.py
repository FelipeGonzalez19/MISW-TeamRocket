# app/locustfile.py

import uuid
from locust import HttpUser, task, between


class ImagenAPITest(HttpUser):
    wait_time = between(1, 3)
    imagen_id = None

    @task
    def listar_imagenes(self):
        """Prueba para listar todas las imágenes."""
        response = self.client.get("/imagenes")
        print(f"🟢 GET /imagenes - {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            if data:
                self.imagen_id = data[0]["id"]

    @task
    def registrar_imagen(self):
        """Prueba para registrar una nueva imagen con ID generado."""
        imagen_data = {
            "id": str(uuid.uuid4()),
            "tipo_imagen": "Rayos X",
            "region_anatomica": "Torax",
            "origen_datos": "Torax",
            "data": {"resolucion": "1024x768", "formato": "DICOM"},
        }

        response = self.client.post(
            "/imagenes",
            json=imagen_data,
            headers={"Content-Type": "application/json"},
        )

        print(f"🔴 POST /imagenes - {response.status_code}")

        if response.status_code in [200, 201]:
            self.imagen_id = response.json().get("id")

    @task
    def obtener_imagen(self):
        """Prueba para obtener una imagen específica si hay una disponible."""
        if self.imagen_id:
            response = self.client.get(f"/imagenes/{self.imagen_id}")
            print(f"🟠 GET /imagenes/{self.imagen_id} - {response.status_code}")

    @task
    def procesar_imagen(self):
        """Prueba para procesar una imagen existente."""
        if self.imagen_id:
            response = self.client.post(f"/imagenes/procesar/{self.imagen_id}")
            print(
                f"🔵 POST /imagenes/procesar/{self.imagen_id} - {response.status_code}"
            )


if __name__ == "__main__":
    import os

    os.system("locust")
