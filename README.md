# Muestra de Cloud Run Hello World

Esta muestra muestra cómo implementar una aplicación Hello World en Cloud Run.

[![Run in Google Cloud][run_img]][run_link]

[run_img]: https://storage.googleapis.com/cloudrun/button.svg
[run_link]: https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&cloudshell_working_dir=run/helloworld

## Construir

''
docker build --tag helloworld: python.
''

## Ejecutar localmente

''
Docker ejecutar --rm -p 9090: 8080 -e PUERTO = 8080 helloworld: python
''

## Prueba

''
pytest
''

_Nota: es posible que deba instalar `pytest` usando` pip install pytest` ._

## Implementar

```sh
# Configura una variable de entorno con tu ID de proyecto de GCP
export GOOGLE_CLOUD_PROJECT=<PROJECT_ID>

# Envía una compilación con Google Cloud Build
gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/helloworld

# Implementar en Cloud Run
gcloud run deploy helloworld \
--image gcr.io/${GOOGLE_CLOUD_PROJECT}/helloworld
```
