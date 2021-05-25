import os
import subprocess
from urllib import request
import uuid

import pytest

# Sufijo único para crear nombres de servicios distintos
SUFFIX = uuid.uuid4().hex[:10]
PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
IMAGE_NAME = f"gcr.io/{PROJECT}/helloworld-{SUFFIX}"


@pytest.fixture
def container_image():
    # Crea una imagen de contenedor para la implementación de Cloud Run
    subprocess.run(
        [
            "gcloud",
            "builds",
            "submit",
            "--tag",
            IMAGE_NAME,
            "--project",
            PROJECT,
            "--quiet",
        ],
        check=True,
    )

    yield IMAGE_NAME

    # Borrar la imagen del contenedor
    subprocess.run(
        [
            "gcloud",
            "container",
            "images",
            "delete",
            IMAGE_NAME,
            "--quiet",
            "--project",
            PROJECT,
        ],
        check=True,
    )


@pytest.fixture
def deployed_service(container_image):
    # Deploy image to Cloud Run
    service_name = f"helloworld-{SUFFIX}"
    subprocess.run(
        [
            "gcloud",
            "run",
            "deploy",
            service_name,
            "--image",
            container_image,
            "--project",
            PROJECT,
            "--region=us-central1",
            "--platform=managed",
            "--no-allow-unauthenticated",
            "--set-env-vars=NAME=Test",
        ],
        check=True,
    )

    yield service_name

    subprocess.run(
        [
            "gcloud",
            "run",
            "services",
            "delete",
            service_name,
            "--platform=managed",
            "--region=us-central1",
            "--quiet",
            "--project",
            PROJECT,
        ],
        check=True,
    )


@pytest.fixture
def service_url_auth_token(deployed_service):
    # Obtenemos el token de autenticación y la URL del servicio Cloud Run
    service_url = (
        subprocess.run(
            [
                "gcloud",
                "run",
                "services",
                "describe",
                deployed_service,
                "--platform=managed",
                "--region=us-central1",
                "--format=value(status.url)",
                "--project",
                PROJECT,
            ],
            stdout=subprocess.PIPE,
            check=True,
        )
        .stdout.strip()
        .decode()
    )
    auth_token = (
        subprocess.run(
            ["gcloud", "auth", "print-identity-token"],
            stdout=subprocess.PIPE,
            check=True,
        )
        .stdout.strip()
        .decode()
    )

    yield service_url, auth_token

    # no es requerido el borrado de la imagen


def test_end_to_end(service_url_auth_token):
    service_url, auth_token = service_url_auth_token

    req = request.Request(
        f"{service_url}/", headers={"Authorization": f"Bearer {auth_token}"}
    )
    response = request.urlopen(req)
    assert response.status == 200

    body = response.read()
    assert "Hello Test!" == body.decode()
