import os
import shutil
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

SourceFolder = "G:\Mi unidad\Plex\\"
print(SourceFolder)
nombreSerie = input('¿Cuál es el nombre de la serie?: ')
TemporadaSerie = input('¿Cuál es la temporada de la serie? (01, 02, 03, etc): ')

listaCarpetas = os.listdir(SourceFolder) #Listado de carpetas dentro de SourceFolder
os.mkdir(SourceFolder + nombreSerie) #Creación de carpeta con el nombre de la serie
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
            try:
                shutil.move(folder + newName, SourceFolder + nombreSerie)
            except:
                os.rename(folder + newName, folder + oldName)
                print(listaFicheros[i])
                numeroEpisodio = input(bcolors.WARNING + 'WARNING: El número de episodio que has introducido ya existe, ¿Qué episodio es?: '+bcolors.ENDC)
                newName=nombreSerie + " S" + TemporadaSerie + "E" + str(numeroEpisodio) + "." + extension
                os.rename(folder + oldName, folder + newName)
                shutil.move(folder + newName, SourceFolder + nombreSerie)
        os.rmdir(folder)
listaCarpetasSeries = os.listdir(SourceFolder+"Series")
if (nombreSerie in listaCarpetasSeries): #Si la carpeta ya existe en Series
    listaFicheros = os.listdir(SourceFolder + nombreSerie)
    for i in range(len(listaFicheros)):
        shutil.move(SourceFolder + nombreSerie + "\\" + listaFicheros[i], SourceFolder+"Series\\"+nombreSerie)
    os.rmdir(SourceFolder + nombreSerie)
else:
    shutil.move(SourceFolder + nombreSerie, SourceFolder+"Series")
input(bcolors.OKGREEN+'Proceso finalizado exitosamente. Presiona ENTER para salir'+bcolors.ENDC)