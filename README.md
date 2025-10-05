# API dockenizada

**Objetivo**.- Crear una api sencilla junto con docker para poder montarla en la plataforma Render

**Requisitos**
1.- tener instalado python
2.- tener instalada la libreria virtualenv puedes checar tus librerias instaladas con pip list 

**Paso 1** Crear una carpeta llamada retoApi y dentro de esta crear un entorno virtual de python 
para que solamente se instalen las librerias a usar y no llevarnos más al hacer el archivo requirements.txt
Crea una carpeta 
```
virtualenv <Nombre del entorno>
.\<Nombre del entorno>\Scripts\activate
```
**Paso 2** Desarrollar los metodos de la api y probarla, con el siguiente comando se levanta el servicio web de la api
```
uvicorn main:app --reload
```
