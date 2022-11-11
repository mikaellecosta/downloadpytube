from time import sleep
from pytube import YouTube
from pytube import Playlist
import os
import sys
from tkinter import *

def main():
    print("\n### Seja bem-vindo ao Mika Downloader ###\n© Programa desenvolvido em Python por Mikaelle Costa - Graduanda em Ciência da Computacão\n")
    print(" --- O QUE DESEJA BAIXAR? ---\n -> (1) MUSICA\n -> (2) VIDEO\n -> (3) PLAYLIST MUSICA\n -> (4) PLAYLIST VIDEO\n -> (5) SAIR\n")
    opcao = int(input("Digite sua opcao: "))
    
    if (opcao == 5):
        print("O programa será encerado. Obrigada por testar!")
        sleep(1)
        sys.exit(0)
        
    elif(opcao < 1 or opcao > 5):
        print("Numero invalido! Digite novamente\n")
        sleep(1)
        return main()
    else:

        url =  str(input("Digite a URL: "))

        if (opcao == 1):
            BaixarMusica(url)

        elif (opcao == 2):
            BaixarVideo(url)

        elif (opcao == 3):
            url = Playlist(str(url))
            BaixarPlylstMusica(url)
        elif (opcao == 4):
            url = Playlist(str(url))
            BaixarPlylstVideo(url)
         
def BaixarMusica(url):
    musica = YouTube(url)
    print("Nome da musica: " + musica.title)
    confirm = str(input("Baixar? S/N\n"))

    if (confirm == 'S' or confirm == 's'):
        print("----- iniciando download -----")
        format = musica.streams.filter(only_audio=True).first()
        out = format.download(output_path='MikaDownloader')

        base, ext = os.path.splitext(out)
        new_file = base + '.mp3'
        os.rename(out, new_file)
        print("----- Download efetuado com sucesso! -----")

        loop = str(input("Deseja realizar outro download? S/N\n"))

        if (loop == 'S' or loop == 's'):
            return main()
    else:
        print("O programa será encerado. Obrigada por testar!")
        sleep(1)
    
def BaixarVideo(url):
    video = YouTube(url)
    print("Nome do video: " + video.title)
    confirm = str(input("Baixar? S/N\n"))

    if (confirm == 'S' or confirm == 's'):
        print("----- iniciando download -----")
        format = video.streams.get_highest_resolution()
        format.download(output_path='MikaDownloader')

        print("----- Download efetuado com sucesso! -----")
        print("O programa será encerado. Obrigada por testar! A mika a")
        
        loop = str(input("Deseja realizar outro download? S/N\n"))

        if (loop == 'S' or loop == 's'):
            return main()
    else:
        print("O programa será encerado. Obrigada por testar!")
        sleep(1)

def BaixarPlylstMusica(url):
    
    print("Nome da playlist:" + url.title)

    confirm = str(input("Baixar? S/N\n"))

    if (confirm == 'S' or confirm == 's'):
        print("----- iniciando download -----")

        for video in url.videos:
            format = video.streams.filter(only_audio=True).first()
            out = format.download(output_path='MikaDownloader')

            base, ext = os.path.splitext(out)
            new_file = base + '.mp3'
            os.rename(out, new_file)
            print("----- Download efetuado com sucesso! -----")

        loop = str(input("Deseja realizar outro download? S/N\n"))

        if (loop == 'S' or loop == 's'):
            return main()
    else:
        print("O programa será encerado. Obrigada por testar!")
        sleep(1)

def BaixarPlylstVideo(url):

    print("Nome da playlist:" + url.title)

    confirm = str(input("Baixar? S/N\n"))

    if (confirm == 'S' or confirm == 's'):
        print("----- iniciando download -----")

        for video in url.videos:
            format = video.streams.get_highest_resolution()
            format.download(output_path='MikaDownloader')

        loop = str(input("Deseja realizar outro download? S/N\n"))

        if (loop == 'S' or loop == 's'):
            return main()
    else:
        print("O programa será encerado. Obrigada por testar!")
        sleep(1)


janela = Tk()
janela.title("Mika Downloader")

texto_orientacao = Label(janela, text="Olá, Bem-vindo! Clique para iniciar o programa.")
texto_orientacao.grid(column=0, row=0)

botao = Button(janela, text="Iniciar", command=main)
botao.grid(column=0, row=1)


janela.mainloop()







