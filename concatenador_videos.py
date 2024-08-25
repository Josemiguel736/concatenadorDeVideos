from moviepy.editor import VideoFileClip, concatenate_videoclips
import pathlib
input_dir=input("Indica la ruta de acceso RELATIVA ")
input_duration=input("Indica la duración máxima de los archivos que quieres que escoja en segundos ")
# Directorio principal donde se encuentran las carpetas
dir_principal = pathlib.Path(input_dir)

# Iteramos sobre cada carpeta en el directorio principal
for carpeta in dir_principal.iterdir():
    if carpeta.is_dir():  # Verificamos que sea una carpeta
        videos = []
        for video_file in sorted(carpeta.iterdir()):  # Ordena los archivos alfabéticamente
            # Verificamos que sea un archivo de video
            if video_file.suffix in ['.mp4', '.avi', '.mov']:
                video=VideoFileClip(str(video_file))
                if float(video.duration)<float(input_duration):
                    videos.append(video)

        if videos:  # Si hay videos en la lista, los concatenamos
            completo = concatenate_videoclips(videos)
            output_file = str(carpeta) + "_completo.mp4"  # Nombre de salida basado en el nombre de la carpeta
            completo.write_videofile(output_file)
        else:
            print(f"No se encontraron videos en la carpeta {carpeta}")

