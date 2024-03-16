def get_image():
    from shutil import copyfile
    try:
        file = open("./vagas.txt", "r", encoding="utf8")
        vagas = open("./allVagas.txt", "r", encoding="utf8")
    
        myLines = file.readlines() #Todas as linhas do arquivo Vagas.
        myVagas = vagas.readlines() #Todas as linhas do arquivo allVagas
    except Exception as e:
        print(e)

    images = [] #Images that i need!
    i = 0
    print("\nLendo Arquivos...\n")
    #Lendo as vagas necessarias
    for lines in myLines:
        lines = lines.replace("\n", "").lower()
        images.append(lines)


    #Adicionando as imagens na pasta
    for aVagas in myVagas:
        aVagas = aVagas.replace("\n","").lower()
        try:
            if images.index(aVagas):
                print("Ok")
                copyfile(f"./images/{aVagas}.jpg", dst=f"./imaged/{aVagas}.jpg")
        except Exception as e:
            pass


    #Fechando os arquivos para evitar bugs ou falhas.
    vagas.close()
    file.close()
    print("\nPrograma Finalizado!")


if __name__ == "__main__":
    print("Iniciando Projeto...\n")
    get_image()