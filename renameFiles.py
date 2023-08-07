import os
import shutil
SourceFolder = "G:\Mi unidad\Plex\\"
print(SourceFolder)
nombreSerie = input('¿Cuál es el nombre de la serie?: ')
TemporadaSerie = input('¿Cuál es la temporada de la serie? (01, 02, 03, etc): ')

subcarpetaName = input('Nombre de la subcarpeta: ') +"\\"

if(subcarpetaName=="\\"):
    print("Los ficheros deben estar en una subcarpeta")
else:
    folder = SourceFolder + subcarpetaName
    listaFicheros = os.listdir(folder)
    print(listaFicheros)

    for i in range(len(listaFicheros)):
        numeroEpisodio = (i+1)
        oldName=listaFicheros[i]
        extension=oldName.split(".")
        extension=extension[len(extension)-1]
        newName=nombreSerie + " S" + TemporadaSerie + "E" + str(numeroEpisodio) + "." + extension
        os.rename(folder + oldName, folder + newName)
        
shutil.move(folder, SourceFolder+"Series")