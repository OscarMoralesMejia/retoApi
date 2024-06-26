# API dockenizada

**Objetivo**.- Crear una api junto con docker para poder montarla en la plataforma Render

**Paso 1** Crear una carpeta llamada retoApi y dentro de esta crear un entorno virtual de python para que solamente se instalen las librerias a usar y no llevarnos más al hacer el archivo requirements.txt
```
virtualenv <Nombre del entorno>
.\<Nombre del entorno>\Scripts\activate
```
**Paso 2** Desarrollar los metodos de la api y probarla, con el siguiente comando se levanta el servicio web de la api
```
uvicorn main:app --reload
```
