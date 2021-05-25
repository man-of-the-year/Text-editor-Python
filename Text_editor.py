from tkinter import*
from tkinter import filedialog,colorchooser,font
from tkinter.messagebox import*
from tkinter.filedialog import*
import os

def change_color():
    text_color = colorchooser.askcolor()
    text_area.config(fg=text_color[1])
    
def change_font(*arguments):
    text_area.config(font=(font_name.get(),size_box.get()))

def new_file():
    wind.title('Untitle')
    text_area.delete(1.0,END)

def paste():
    text_area.event_generate('<<Paste>>')

def copy():
    text_area.event_generate('<<Copy>>')

def cut():
    text_area.event_generate('<<Cut>>')

def save_file():
    file = filedialog.asksaveasfilename(initialfile='unitetled.txt'
    ,defaultextension='.txt',filetype=[('All files','*.*'),('Text document','*.txt')])

    if file is None:
        return
    else:
        try:
            wind.title(os.path.basename(file))
            file = open(file,'w')
            file.write(text_area.get(1.0,END))
        except Exception: 
            print('Couldn`t save')
        finally:
            file.close()
    

def about():
    showinfo('About','U write a editor!!')

def open_file():
    file = filedialog.askopenfilename(defaultextension='.txt',file=[('All files','*.*'),('Text documents','*.txt')])

    try:
        wind.title(os.path.basename(file))
        text_area.delete(1.0,END)
        file = open(file,'r')
        text_area.insert(1.0,file.read())

    except  Exception:
        print('Couldn`t read file')
    finally:
        file.close()

def quit():
    wind.destroy()

wind = Tk()
file = None

wind_HEIGHT = 500
wind_WIDTH = 500
screen_HEIGHT = wind.winfo_screenheight()
screen_WIDTH = wind.winfo_screenwidth()

x = int((screen_WIDTH/2)-(screen_WIDTH/2))
y = int((screen_HEIGHT/2)-(screen_HEIGHT/2))

wind.geometry('{}x{}+{}+{}'.format(wind_WIDTH,wind_HEIGHT,x,y))

font_name = StringVar(wind)
font_name.set('Arial')

font_size = StringVar(wind)
font_size.set('25')

text_area = Text(wind,font=(font_name.get(), font_size.get()))
scroll_bar = Scrollbar(text_area)
wind.grid_rowconfigure(0,weight=1)
wind.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N + E + S + W)

scroll_bar.pack(side=RIGHT,fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(wind)
frame.grid()

color_button = Button(frame,command=change_color,text='color')
color_button.grid(row=0,column=0)

font_button = OptionMenu(frame,font_name,command=change_font,*font.families())
font_button.grid(row=0,column=1)

size_box = Spinbox(frame,from_=1,to=70,command=change_font,textvariable=font_size)
size_box.grid(row=0,column=2)

menu_bar = Menu(wind)
wind.config(menu=menu_bar)


file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(command=new_file,label='New')
file_menu.add_command(command=open_file,label='Open')
file_menu.add_command(command=save_file,label='Save')
file_menu.add_separator()
file_menu.add_command(command=quit,label='Exit')
menu_bar.add_cascade(menu=file_menu,label='File')


edit_menu = Menu(menu_bar,tearoff=0) 
edit_menu.add_command(command=cut,label='Cut')
edit_menu.add_command(command=copy,label='Copy')
edit_menu.add_command(command=paste,label='Paste')
menu_bar.add_cascade(menu=edit_menu,label='Edit')


help_menu = Menu(menu_bar,tearoff=0)
help_menu.add_command(command=about,label='About')
menu_bar.add_cascade(menu=help_menu,label='Help')




wind.mainloop()
