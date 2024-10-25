# My FastAPI App

Esta es una aplicación FastAPI desplegada con Serverless Framework en AWS Lambda.

## Funcionalidades

* Expone una API REST con dos endpoints:
    * `/`: Endpoint raíz que responde a peticiones GET.
    * `/hello/{proxy+}`: Endpoint que responde a peticiones GET y acepta un parámetro dinámico `proxy`.

## Servicios de AWS

* AWS Lambda
* AWS API Gateway (HTTP API)

## Despliegue

1. Asegúrate de tener instalado Serverless Framework y configurado tu AWS CLI.
2. Clona este repositorio.
3. Instala las dependencias: `npm install`
4. Despliega la aplicación: `sls deploy`

## Ejecución local

1. Instala las dependencias: `npm install`
2. Inicia el servidor local: `sls offline start`

## Uso

Una vez desplegada, puedes acceder a la API en la URL proporcionada por Serverless Framework.

* **Endpoint raíz:** `GET /`
* **Endpoint con parámetro:** `GET /hello/nombre` (reemplaza `nombre` con el valor deseado)

## Contribuciones

Siéntete libre de contribuir a este proyecto.

## Licencia

MIT