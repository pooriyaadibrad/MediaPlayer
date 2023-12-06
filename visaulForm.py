import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pygame

class App(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.CreateWiget()
    def CreateWiget(self):
        #playbtn
        self.ImgPlay=PhotoImage(file="image/play.png")
        self.ImgNext=PhotoImage(file="image/Next.png")
        self.ImgUndo=PhotoImage(file="image/Undo.png")
        self.ImgAddMusic=PhotoImage(file="image/AddMusic.png")
        self.PlaySong=Button(self.master,image=self.ImgPlay)
        self.PlaySong.bind("<Button-1>",self.ClickPlay)
        self.PlaySong.place(x=150,y=200)
        self.UndoSong = Button(self.master, image=self.ImgUndo)
        self.UndoSong.bind("<Button-1>", self.play_song)
        self.UndoSong.place(x=90, y=210)
        self.NextSong = Button(self.master, image=self.ImgNext)
        self.NextSong.bind("<Button-1>", self.play_song)
        self.NextSong.place(x=220, y=210)
        self.SelectFolderBtn = Button(self.master, image=self.ImgAddMusic)
        self.SelectFolderBtn.bind("<Button-1>", self.SelectFolder)
        self.SelectFolderBtn.place(x=300, y=350)
        #table
        self.Table=ttk.Treeview(win,columns=("c1"),show="headings")
        self.Table.column("c1",width=250,anchor="center")
        self.Table.heading("c1",text="Music")
        self.Table.pack(side="right",fill=BOTH)
    def SelectFolder(self,e):
        Files=filedialog.askdirectory()
        FileInFolder=os.listdir(Files)
        for File in FileInFolder:
            if File.endswith(".mp3"):
                self.Table.insert('',"end",values=[File])
    def load_songs(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".mp3"):
                    self.song_list.append(os.path.join(root, file))

    def ClickPlay(self,e):
        pass
    def play_song(self,song_index):
        pygame.mixer.music.load(self.song_list[song_index])
        pygame.mixer.music.play()

if __name__=="__main__":
    win=Tk()

    win.geometry("%dx%d+%d+%d"%(600,400,250,50))
    app1=App(win)


    win.mainloop()