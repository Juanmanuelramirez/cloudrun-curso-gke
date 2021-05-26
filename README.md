# Muestra de Cloud Run Hello World

Esta muestra muestra cómo implementar una aplicación Hello World en Cloud Run.

[![Run in Google Cloud][run_img]][run_link]

[run_img]: https://storage.googleapis.com/cloudrun/button.svg
[run_link]: https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&cloudshell_working_dir=run/helloworld

## Clonamos nuestro repositorio

```sh
git clone https://github.com/Juanmanuelramirez/cloudrun-curso-gke.git
```

## Construir
_Nota: Recuerda obtener el Id de tu proyecto y sustituirlo antes de correr esta instrucción._

```sh
export GOOGLE_CLOUD_PROJECT=$(gcloud config get-value project)
gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/helloword
```

## Implementación en Cloud Run

```sh
gcloud run deploy --image gcr.io/${GOOGLE_CLOUD_PROJECT}/helloword --platform managed
```
_a) Se solicitará el nombre del servicio, presiona enter para aceptar el nombre predeterminado `helloworld`._

_b) Se solicitará la región, seleccionas la region que mas se adapte a tu localización, por ejemplo, `us-central1`._


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
