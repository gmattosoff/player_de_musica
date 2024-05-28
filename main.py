from tkinter import *
from pygame import mixer

janela = Tk()
janela.title('Player de Música')
janela.geometry("334x365")
janela.resizable(False, False)

mixer.init()
pausado = False
song_tocando = ''

def tocar(song):
    global song_tocando
    mixer.music.stop()
    
    mixer.music.load(f'songs/{song}.mp3')
    mixer.music.play()
    mixer.music.set_volume(0.2)
    pause_btn = Button(control_frame, image=pause_img, borderwidth=0, command=pausar)
    pause_btn.grid(row=0, column=1, padx=5)
    
    musica_tocada = song.replace(' ', '').capitalize()
    
    for botao_nome, botao_visual in botoes:
        botao_nome = botao_nome.replace(' ', '').capitalize()
        if botao_nome == musica_tocada:
            botao_visual.config(bg='lightgreen')
        else:
            botao_visual.config(bg='SystemButtonFace')
            
    song_tocando = song

def pausar():
    global pausado, pause_btn
    if not pausado:
        mixer.music.pause()
        pausado = True
        pause_btn = Button(control_frame, image=play_img, borderwidth=0, command=pausar)
    else:
        play_img
        mixer.music.unpause()
        pausado = False
        pause_btn = Button(control_frame, image=pause_img, borderwidth=0, command=pausar)
    pause_btn.grid(row=0, column=1, padx=5)

def proxima():
    global song_tocando
    if song_tocando != 'happyday':
        index_atual = songs.index(song_tocando)
        proximo_index = (index_atual + 1)
        tocar(songs[proximo_index])
        song_tocando = songs[proximo_index]
    else:
        tocar('violin')

def anterior():
    global song_tocando
    if song_tocando != 'violin':
        index_atual = songs.index(song_tocando)
        anterior_index = (index_atual - 1)
        tocar(songs[anterior_index])
        song_tocando = songs[anterior_index]
    else:
        tocar('happyday')

def criar_botao(texto, row, command):
    button = Button(
        janela,
        command=command,
        height=2,
        width=36,
        text=texto,
        font=('Arial',13)
    )
    button.grid(row=row)
    return texto, button

songs = ['violin','calling','citylights','yourlove','robotcoupe','happyday']

botoes = [
    criar_botao('Violin', 0, lambda: tocar('violin')),
    criar_botao('Calling', 1, lambda: tocar('calling')),
    criar_botao('City Lights', 2, lambda: tocar('citylights')),
    criar_botao('Your Love', 3, lambda: tocar('yourlove')),
    criar_botao('Robot Coupe', 4, lambda: tocar('robotcoupe')),
    criar_botao('Happy Day', 5, lambda: tocar('happyday'))
]

play_img = PhotoImage(file='imgs/play.png')
pause_img = PhotoImage(file='imgs/pause.png')
next_img = PhotoImage(file='imgs/next.png')
prev_img = PhotoImage(file='imgs/previous.png')

control_frame = Frame(janela)
control_frame.grid(row=6, pady=12)

pause_btn= Button(control_frame, image=play_img, borderwidth=0, command=pausar)
next_btn = Button(control_frame, image=next_img, borderwidth=0, command=proxima)
prev_btn = Button(control_frame, image=prev_img, borderwidth=0, command=anterior)

prev_btn.grid(row=0, column=0, padx=5)
pause_btn.grid(row=0, column=1, padx=5)
next_btn.grid(row=0, column=2, padx=5)

janela.mainloop()