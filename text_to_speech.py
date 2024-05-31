from gtts import gTTS
from pydub import AudioSegment
import os

def text_to_speech(text, filename, lang='es'):
    # Divide el texto en fragmentos si es necesario
    max_chars = 5000  # Límite de caracteres por fragmento
    text_chunks = [text[i:i + max_chars]
                   for i in range(0, len(text), max_chars)]

    # Convertir cada fragmento a un archivo temporal MP3
    temp_files = []
    for i, chunk in enumerate(text_chunks):
        # tld='com' para un acento más neutral
        tts = gTTS(text=chunk, lang=lang, tld='com')
        temp_file = f"temp_{i}.mp3"
        tts.save(temp_file)
        temp_files.append(temp_file)

    # Combinar todos los archivos MP3 temporales en uno solo
    combined_audio = AudioSegment.empty()
    for temp_file in temp_files:
        audio = AudioSegment.from_mp3(temp_file)
        combined_audio += audio
        os.remove(temp_file)  # Eliminar archivo temporal

    # Exportar el archivo combinado a MP3
    combined_audio.export(filename, format="mp3")


if __name__ == "__main__":
    # Ejemplo de uso con texto en múltiples líneas
    text = """
    Hola, ¿cómo estás?  Espero que estés bien.
    Este es un ejemplo de texto a voz.
    
    ¡Hasta luego!
    
    """

    filename = "output.mp3"
    text_to_speech(text, filename)
    print(f"Archivo MP3 guardado como {filename}")
