#importing libraries 
import pygame 
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
from mutagen.mp3 import MP3
import time
import tkinter.ttk as ttk
from tkinter import messagebox
#add song fun
def addsong():
    temp_song=filedialog.askopenfilename(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    temp_song=temp_song.replace("C:/Users/Parth/Music/","")
    temp_song=temp_song.replace(".mp3","")
    songs_list.insert(END,temp_song)
#add many songs to the playlist
def addsongs():
    #a list of songs is returned 
    temp_songs=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    #loop through everyitem in the list
    for temp_song in temp_songs:
        temp_song=temp_song.replace("C:/Users/Parth/Music/","")
        temp_song=temp_song.replace(".mp3","")
        
        songs_list.insert(END,temp_song)
        
        
            
def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])
    
    
def Play():
    temp_song=songs_list.get(ACTIVE)
    temp_song=f'C:/Users/Parth/Music/{ temp_song}.mp3'
    pygame.mixer.music.load(temp_song)
    pygame.mixer.music.play()
    play_time()
    slider_position=int(song_length)
    my_slider.config(to=slider_position,value=0)

#to pause the song 
def Pause():
    pygame.mixer.music.pause()

#to stop the  song 
def Stop():
    pygame.mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

#to resume the song

def Resume():
    pygame.mixer.music.unpause()

#Function to navigate from the current song
def Previous():
   #to get the selected song index
    next_one=songs_list.curselection()
    #to get the next song index
    next_one=next_one[0]-1
    #to get the next song 
    temp_song=songs_list.get(next_one)
    temp_song=f'C:/Users/Parth/Music/{temp_song}.mp3'
    pygame.mixer.music.load(temp_song)
    pygame.mixer.music.play(loops=0)
    songs_list.selection_clear(0,END)
    #activate newsong
    songs_list.activate(next_one)
     #set the next song
    songs_list.selection_set(next_one,last=None)



def Next():
    #to get the selected song index
    next_one=songs_list.curselection()
    #to get the next song index
    
    next_one=next_one[0]+1
    #to get the next song 
    temp_song=songs_list.get(next_one)
    temp_song=f'C:/Users/Parth/Music/{temp_song}.mp3'
    pygame.mixer.music.load(temp_song)
    pygame.mixer.music.play(loops=0)
    songs_list.selection_clear(0,END)
    #activate newsong
    songs_list.activate(next_one)
     #set the next song
    songs_list.selection_set(next_one,last=None)

#creating the root window 
root=Tk()
root.title('DataFlair Music player App ')
root.geometry("500x450")



#initialize mixer 
pygame.mixer.init()
def play_time():
    current_time=pygame.mixer.music.get_pos() /1000
    converted_current_time= time.strftime('%M:%S', time.gmtime(current_time))
    #get currently playing song
    #current_song=songs_list.curselection() 
    temp_song=songs_list.get(ACTIVE)
    temp_song=f'C:/Users/Parth/Music/{temp_song}.mp3'
    #get song lenght with mutagen
    song_mut=MP3(temp_song)
    global song_length 
    song_length=song_mut.info.length
    converted_song_length= time.strftime('%M:%S', time.gmtime(song_length))
    
    status_bar.config(text=f' Time Elapsed :{converted_current_time} of    {converted_song_length}  ' )
    my_slider.config(value=int(current_time))
    
    status_bar.after(1000,play_time)
#create slider function
def slide(x):
    slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}' )
#create the listbox to contain songs
songs_list=Listbox(root,selectmode=SINGLE,bg="light green",fg="black",font=('arial',15),height=20,width=50,selectbackground="gray",selectforeground="black")

songs_list.pack(expand=True,fill=BOTH)

#font is defined which is to be used for the button font 
defined_font = font.Font(family='Helvetica')

#play button
play_button=Button(root,text="Play",width =7,command=Play)
play_button['font']=defined_font
play_button.pack(side=LEFT)

#pause button 
pause_button=Button(root,text="Pause",width =7,command=Pause)
pause_button['font']=defined_font
pause_button.pack(side=LEFT)

#stop button
stop_button=Button(root,text="Stop",width =7,command=Stop)
stop_button['font']=defined_font
stop_button.pack(side=LEFT)

#resume button
Resume_button=Button(root,text="Resume",width =7,command=Resume)
Resume_button['font']=defined_font
Resume_button.pack(side=LEFT)

#previous button
previous_button=Button(root,text="Prev",width =7,command=Previous)
previous_button['font']=defined_font
previous_button.pack(side=LEFT)

#nextbutton
next_button=Button(root,text="Next",width =7,command=Next)
next_button['font']=defined_font
next_button.pack(side=LEFT)

#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)
#create status bar
status_bar=Label(root,text='',bd=1,relief=GROOVE,anchor=E)
status_bar.pack(fill= X,side=BOTTOM,ipady=2)
#create slider
my_slider  = ttk.Scale(root,from_=0,to=100, orient=HORIZONTAL,value=0,command=slide ,length=360)
my_slider.pack(pady=30)
#create temporary slider label
slider_label=Label(root,text="0")
slider_label.pack(pady=10)

mainloop()
