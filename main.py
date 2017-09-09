from tkinter import *
from game import RPS


root = Tk()
root.title('Rock Paper Scissors')


def choice_button(x):
    match = RPS.throw(x)
    result.set(match[0])
    session_record.set(RPS.display_s_rec())
    player_icon.delete('all')
    cpu_icon.delete('all')
    player_icon.create_image(2, 2, anchor='nw', image=mirror_icons[x])
    cpu_icon.create_image(2, 2, anchor='nw', image=icons[match[1]])



def quit_button():
    RPS.save_record()
    root.destroy()



result = StringVar()
session_record = StringVar(value=RPS.display_s_rec())
lifetime_record = StringVar(value=RPS.display_l_rec())
icons = [PhotoImage(file='images/rock.gif'), PhotoImage(file='images/paper.gif'), PhotoImage(file='images/scissors.gif')]
mirror_icons = [PhotoImage(file='images/flip_rock.gif'), PhotoImage(file='images/flip_paper.gif'), PhotoImage(file='images/flip_scissors.gif')]

mainframe = Frame(root, relief='sunken', bd=3, height=500, width=500, padx=10, pady=10)
mainframe.pack()

#LABELS#
player_label = Label(mainframe)

game_label = Label(mainframe,width=30, textvariable=result)
game_label.grid(row=3,column=2, columnspan=3)

vs_label = Label(mainframe, text='VS.')
vs_label.grid(row=2, column=3)

l_rec_label = Label(mainframe, textvariable=lifetime_record)
l_rec_label.grid(row=0, column=7, sticky='w')

l_rec_title = Label(mainframe, text='Lifetime Record:', width=16)
l_rec_title.grid(row=0, column=6, sticky='e')

s_rec_label = Label(mainframe, textvariable=session_record)
s_rec_label.grid(row=1, column=7, sticky='w')

s_rec_title = Label(mainframe, text="Session Record:", width=16)
s_rec_title.grid(row=1, column=6, sticky='e')


#FRAMES#
spacer = Frame(mainframe, width=10)
spacer.grid(row=0, column=1)


#CANVASES#
player_icon = Canvas(mainframe, width=100, height=100)
player_icon.create_image(2, 2, anchor='nw', image=mirror_icons[0])
player_icon.grid(row=0, rowspan=3, column=2, sticky='e')

cpu_icon = Canvas(mainframe, width=100, height=100)
cpu_icon.create_image(2, 2, anchor='nw', image=icons[0])
cpu_icon.grid(row=0, rowspan=3, column=4, sticky='e')


#BUTTONS#
q_button = Button(mainframe, text='Save/Quit', command=quit_button)
q_button.grid(sticky='SE', row=3, column=7)

r_button = Button(mainframe, width=10, text='Rock', command=lambda: choice_button(0))
r_button.grid(sticky=W, row=0, column=0)

p_button = Button(mainframe, width=10, text='Paper', command=lambda: choice_button(1))
p_button.grid(sticky=W, row=1, column=0)

s_button = Button(mainframe, width=10, text='Scissors', command=lambda: choice_button(2))
s_button.grid(sticky=W, row=2, column=0)



if __name__ == "__main__":
    root.mainloop()
