import os
import shutil
SourceFolder = "G:\Mi unidad\Plex\\"
print(SourceFolder)
nombreSerie = input('¿Cuál es el nombre de la serie?: ')
TemporadaSerie = input('¿Cuál es la temporada de la serie? (01, 02, 03, etc): ')

listaCarpetas = os.listdir(SourceFolder)
os.mkdir(SourceFolder + nombreSerie)
for i in range(len(listaCarpetas)):
    if(listaCarpetas[i] == "Series" or listaCarpetas[i] == "Peliculas" or listaCarpetas[i] == "renameFiles.py"):
        print("no se toca la carpeta " + listaCarpetas[i])
    else:
        subcarpetaName = listaCarpetas[i] + "\\"
        folder = SourceFolder + subcarpetaName
        listaFicheros = os.listdir(folder)

        for i in range(len(listaFicheros)):
            print(listaFicheros[i])
            numeroEpisodio = input('¿Qué episodio es este?: ')
            oldName=listaFicheros[i]
            extension=oldName.split(".")
            extension=extension[len(extension)-1]
            newName=nombreSerie + " S" + TemporadaSerie + "E" + str(numeroEpisodio) + "." + extension
            os.rename(folder + oldName, folder + newName)
            shutil.move(folder + newName, SourceFolder + nombreSerie)
        os.rmdir(folder)
shutil.move(SourceFolder + nombreSerie, SourceFolder+"Series")