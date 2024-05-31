# Text-to-Speech Conversion

Este repositorio contiene un script de Python para convertir texto a voz y combinar los archivos de audio en formato MP3 utilizando `gTTS` y `pydub`.

## Requisitos

- Python 3.6 o superior
- ffmpeg

## Instalación

### Paso 1: Clonar el repositorio

Clona este repositorio en tu máquina local.

```git clone <URL_DEL_REPOSITORIO>```

```cd <NOMBRE_DEL_REPOSITORIO>```

### Paso 2: Instalar las dependencias

Instala las dependencias de Python utilizando `pip`.

```pip install -r requirements.txt```


### Paso 3: Configurar ffmpeg

Asegúrate de que `ffmpeg` esté instalado y en el PATH del sistema. Puedes incluir la carpeta `ffmpeg` proporcionada en este repositorio y agregarla al PATH.

#### Incluir ffmpeg en el PATH

1. Copia la carpeta `ffmpeg` proporcionada en este repositorio a `C:\ffmpeg` o de preferencia. Utilizaremos esta ruta para este ejemplo.
2. Agrega `C:\ffmpeg\bin` al PATH del sistema:

- Abre el Panel de Control y navega a `Sistema` -> `Configuración avanzada del sistema`.
- Haz clic en el botón `Variables de entorno`.
- En la sección `Variables del sistema`, encuentra la variable `Path` y selecciónala. Luego haz clic en `Editar`.
- Haz clic en `Nuevo` y agrega `C:\ffmpeg\bin`.
- Guarda los cambios y cierra las ventanas.

3. Verifica la instalación de `ffmpeg`:

```ffmpeg -version```
```ffprobe -version```

## Uso

Para usar el script y convertir texto a voz, sigue los siguientes pasos:

1. Abre una terminal y navega al directorio del repositorio.
2. Ejecuta el script `text_to_speech.py` con el texto que deseas convertir.
3. En la raíz del script verás un `output.mp3` o el nombre que cambiaste en la variable `filename`.


## Convertir MP3 a WAV (Opcional)
Si necesitas convertir el archivo MP3 resultante a WAV, puedes usar ffmpeg desde la línea de comandos:
```ffmpeg -i output.mp3 output.wav```



## Problemas Comunes

- `pydub.exceptions.CouldntDecodeError`
Si encuentras un error relacionado con `ffmpeg` o `ffprobe`, asegúrate de que `ffmpeg` esté correctamente instalado y en el PATH del sistema.

- `gTTS` no genera archivos válidos
Asegúrate de que `gTTS` esté instalado y actualizado. Si el problema persiste, verifica tu conexión a internet ya que `gTTS` requiere acceso a Google Translate.


##  Licencia
Este proyecto está licenciado bajo los términos de la licencia MIT. Consulta el archivo LICENSE para más información.