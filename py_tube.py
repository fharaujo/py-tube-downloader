from pytube import YouTube, Playlist

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('\n ** Py-Tube-Youtube Download ***')
print('Todo vídeo é baixado na qualidade 720p (Se estiver disponível)\n')
print('Opções do programa: ')


def init():
    print('*-> [1] Um para escolher DOWNLOAD \n*-> [0] Zero para sair\n')
    try:
        program = int(input('Digite a opção: '))
        if program > 0 and program == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            program_main()
        elif program < 0 or program > 1:
            print('## Opção inválida ##\n')
            init()
    except ValueError:
        print('\n## Digite um opção válida ##\n')
        init()


def program_main():
    option = input('Digite (v) para um VÍDEO ou (p) para PLAYLIST: ').lower()
    if option == 'v':
        link = input('\nCole o link do vídeo aqui: ')
        video = YouTube(link)
        stream = video.streams.filter(progressive=True)
        down_video = video.streams.get_by_itag(22)
        print(f'Download começou... {video.title}')
        down_video.download()
        print('Fim do Download!!!')
    elif option == 'p':
        link = input('\nCole o link da playlist aqui: ')
        playlist = YouTube(link)
        for video in playlist.videos:
            print(f'Download começou... {video.title}')
            video.streams.first().download()
        print('Fim do Download!!!')
    else:
        print('Digite uma oção válida.')
        program_main()


init()
print('\n\nPy-tube-Download - 1.0 - @faraujo')
