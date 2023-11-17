from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from time import strftime

# The class represents the main page of a project prototypes website.
class Project_prototypes_main_page:
    def __init__(self):
        self.window_2 = Tk()
        self.window_2.configure(bg='#00c77e')
        self.window_2.title("My Dreaw World")
        self.window_2.iconbitmap('463407-200.ico')
        self.first_machine = CircularQueue(10000)
        self.second_machine = CircularQueue(10000)
        self.third_machine = CircularQueue(10000)
        self.fouth_machine = CircularQueue(10000)
        self.window_2.protocol("WM_DELETE_WINDOW", self.closing_window)

        self.menu = Menu(self.window_2)
        self.window_2.config(menu=self.menu)
        self.file_menu = Menu(self.menu, tearoff = 0, font=('High Tower Text', 10, 'bold'), bg = 'lightpink')
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Queue Table", command= self.name_table)


        self.fram1 = Frame(self.window_2, bg = '#00c77e')
        self.fram1.grid(row=2, column=1)
        self.fram2 = Frame(self.window_2, bg = '#00c77e')
        self.fram2.grid(row=4, column=1)
        self.fram3 = Frame(self.window_2, bg = '#00c77e')
        self.fram3.grid(row=6, column=1)
        self.fram4 = Frame(self.window_2, bg = '#00c77e')
        self.fram4.grid(row=8, column=1)
        self.fram5 = Frame(self.window_2, bg = '#00c77e')
        self.fram5.grid(row=1, column=2, rowspan=20, columnspan=2, sticky=N+S+E+W, pady =20)

        self.image_path_1 = 'supertrain-gif-maker (1).gif'
        self.image_path_2 = 'supertrain-gif-maker (2).gif'
        self.image_path_3 = 'supertrain-gif-maker (3).gif'
        self.image_path_4 = 'lung-gif-maker.gif'

        scale_factor = 5

        self.pic_1 = PhotoImage(file=self.image_path_1).subsample(scale_factor, scale_factor)
        self.label_1 = Label(self.window_2, image=self.pic_1, width=200, height=150, bg='#00c77e')
        self.label_1.grid(row=2, column=0, padx=50)

        self.pic_2 = PhotoImage(file=self.image_path_2).subsample(scale_factor, scale_factor)
        self.label_2 = Label(self.window_2, image=self.pic_2, width=200, height=150, bg='#00c77e')
        self.label_2.grid(row=4, column=0, padx=50)

        self.pic_3 = PhotoImage(file=self.image_path_3).subsample(scale_factor, scale_factor)
        self.label_3 = Label(self.window_2, image=self.pic_3, width=200, height=150, bg='#00c77e')
        self.label_3.grid(row=6, column=0, padx=50)

        self.pic_4 = PhotoImage(file=self.image_path_4).subsample(scale_factor, scale_factor)
        self.label_4 = Label(self.window_2, image=self.pic_4, width=200, height=150, bg='#00c77e')
        self.label_4.grid(row=8, column=0, padx=50)


        self.button_1 = Button(self.fram1, text='Book', command=lambda: self.command(1), width= 10, font= ('Elephant', 10, 'italic'), bg= '#4d80b3', fg= 'white')
        self.button_2 = Button(self.fram2, text='Book', command=lambda: self.command(2), width= 10, font= ('Elephant', 10, 'italic'), bg= '#4d80b3', fg= 'white')
        self.button_3 = Button(self.fram3, text='Book', command=lambda: self.command(3), width= 10, font= ('Elephant', 10, 'italic'), bg= '#4d80b3', fg= 'white')
        self.button_4 = Button(self.fram4, text='Book', command=lambda: self.command(4), width= 10, font= ('Elephant', 10, 'italic'), bg= '#4d80b3', fg= 'white')
        self.button_1.grid(row= 1, column=1)
        self.button_2.grid(row= 1, column=1)
        self.button_3.grid(row= 1, column=1)
        self.button_4.grid(row= 1, column=1)


        self.time_earth = Label(self.window_2, font=('STHupo', 18),
            background='#00c77e',
            foreground='black')
        self.time_earth.grid(row=1, column=1, padx=50, pady=7, sticky=E)
        self.time()


        self.label_countdown_1 = Label(self.window_2, font=('Ebrima', 12), text = f"Ends in: 00:00:00",
                background='#006b8c',
                foreground='white')
        self.label_countdown_1.grid(row=1, column=0, padx=50, pady=7, sticky=E)

        
        self.button_settime_1 = Button(self.window_2, font=('Impact', 12), text="Set Time", command= lambda: self.settimer(1),
                background='#ff6e75',
                foreground='white')
        self.button_settime_1.grid(row= 1, column=0, padx=50, pady=7, sticky=W)
        

        self.label_countdown_2 = Label(self.window_2, font=('Ebrima', 12), text = f"Ends in: 00:00:00",
                background='#006b8c',
                foreground='white')
        self.label_countdown_2.grid(row=3, column=0, padx=50, pady=7, sticky=E)

        
        self.button_settime_2 = Button(self.window_2, font=('Impact', 12), text="Set Time", command= lambda: self.settimer(2),
                background='#ff6e75',
                foreground='white')
        self.button_settime_2.grid(row= 3, column=0, padx=50, pady=7, sticky=W)
        

        self.label_countdown_3 = Label(self.window_2, font=('Ebrima', 12), text = f"Ends in: 00:00:00",
                background='#006b8c',
                foreground='white')
        self.label_countdown_3.grid(row=5, column=0, padx=50, pady=7, sticky=E)

        
        self.button_settime_3 = Button(self.window_2, font=('Impact', 12), text="Set Time", command= lambda: self.settimer(3),
                background='#ff6e75',
                foreground='white')
        self.button_settime_3.grid(row= 5, column=0, padx=50, pady=7, sticky=W)
        

        self.label_countdown_4 = Label(self.window_2, font=('Ebrima', 12), text = f"Ends in: 00:00:00",
                background='#006b8c',
                foreground='white')
        self.label_countdown_4.grid(row=7, column=0, padx=50, pady=7, sticky=E)

        
        self.button_settime_4 = Button(self.window_2, font=('Impact', 12), text="Set Time", command= lambda: self.settimer(4),
                background='#ff6e75',
                foreground='white')
        self.button_settime_4.grid(row= 7, column=0, padx=50, pady=7, sticky=W)
        
        
        self.ima = 'people_queue_regular_icon_205081.gif'
        scale = 10
        self.im1 = PhotoImage(file=self.ima).subsample(scale, scale)
        self.label_101 = Label(self.fram1, image=self.im1, width=50, height=70, bg='#00c77e')
        self.im2 = PhotoImage(file=self.ima).subsample(scale, scale)
        self.label_102 = Label(self.fram2, image=self.im2, width=50, height=70, bg='#00c77e')
        self.im3 = PhotoImage(file=self.ima).subsample(scale, scale)
        self.label_103 = Label(self.fram3, image=self.im3, width=50, height=70, bg='#00c77e')
        self.im4 = PhotoImage(file=self.ima).subsample(scale, scale)
        self.label_104 = Label(self.fram4, image=self.im4, width=50, height=70, bg='#00c77e')
        self.label_101.grid(row= 2, column=1)
        self.label_102.grid(row= 2, column=1)
        self.label_103.grid(row= 2, column=1)
        self.label_104.grid(row= 2, column=1)


        self.laa1 = Label(self.fram1,bg='#00c77e', text='0', font= ("Segoe UI Black", 10), width=3)
        self.laa2 = Label(self.fram2, bg='#00c77e', text='0', font= ("Segoe UI Black", 10), width=3)
        self.laa3 = Label(self.fram3, bg='#00c77e', text='0', font= ("Segoe UI Black", 10), width=3)
        self.laa4 = Label(self.fram4, bg='#00c77e', text='0', font= ("Segoe UI Black", 10), width=3)
        self.laa1.grid(row= 2, column=2)
        self.laa2.grid(row= 2, column=2)
        self.laa3.grid(row= 2, column=2)
        self.laa4.grid(row= 2, column=2)


        self.name_de_1 = StringVar() 
        self.entry_1_delete = Entry(self.fram1, textvariable = self.name_de_1, font=('YouYuan',10,'normal'))
        self.button_de_1 = Button(self.fram1, text="Delete", command=lambda: self.delete_name(1), width= 10, font= ('Elephant', 10, 'italic'))
        self.entry_1_delete.grid(row= 3, column=1)
        self.button_de_1.grid(row= 3, column=3)

        self.name_de_2 = StringVar() 
        self.entry_2_delete = Entry(self.fram2, textvariable = self.name_de_2, font=('YouYuan',10,'normal'))
        self.button_de_2 = Button(self.fram2, text="Delete", command=lambda: self.delete_name(2), width= 10, font= ('Elephant', 10, 'italic'))
        self.entry_2_delete.grid(row= 3, column=1)
        self.button_de_2.grid(row= 3, column=3)

        self.name_de_3 = StringVar() 
        self.entry_3_delete = Entry(self.fram3, textvariable = self.name_de_3, font=('YouYuan',10,'normal'))
        self.button_de_3 = Button(self.fram3, text="Delete", command=lambda: self.delete_name(3), width= 10, font= ('Elephant', 10, 'italic'))
        self.entry_3_delete.grid(row= 3, column=1)
        self.button_de_3.grid(row= 3, column=3)

        self.name_de_4 = StringVar() 
        self.entry_4_delete = Entry(self.fram4, textvariable = self.name_de_4, font=('YouYuan',10,'normal'))
        self.button_de_4 = Button(self.fram4, text="Delete", command=lambda: self.delete_name(4), width= 10, font= ('Elephant', 10, 'italic'))
        self.entry_4_delete.grid(row= 3, column=1)
        self.button_de_4.grid(row= 3, column=3)


        self.labe0 = Label(self.window_2,text='',pady = 20, bg='#00c77e')
        self.labe0.grid(row=12, column=2)
        self.labe01 = Label(self.window_2,text='', bg='#00c77e', width=5)
        self.labe01.grid(row=5, column=10)

        queue_Num_Roller_Coaster_Train = self.count_back_up_data("Num_Roller_Coaster_Train.txt")
        queue_Num_Tornado = self.count_back_up_data("Num_Tornado.txt")
        queue_Num_Thunder_Bird = self.count_back_up_data("Num_Thunder_Bird.txt")
        queue_Num_Super_Splash = self.count_back_up_data("Num_Super_Splash.txt")

        for i in queue_Num_Roller_Coaster_Train:
            self.first_machine.enqueue(i)
            if i == None:
                self.set_laa1_text('0')
            self.set_laa1_text(str(self.first_machine.get_size_element()))
        for j in queue_Num_Tornado:
            self.second_machine.enqueue(j)
            if j == None:
                self.set_laa1_text('0')
            self.set_laa2_text(str(self.second_machine.get_size_element()))
        for k in queue_Num_Thunder_Bird:
            self.third_machine.enqueue(k)
            if k == None:
                self.set_laa1_text('0')
            self.set_laa3_text(str(self.third_machine.get_size_element()))
        for l in queue_Num_Super_Splash:
            self.fouth_machine.enqueue(l)
            if l == None:
                self.set_laa1_text('0')
            self.set_laa4_text(str(self.fouth_machine.get_size_element()))

        self.window_2.mainloop()

    def closing_window(self):
        if tkinter.messagebox.askyesno(title="Exit?", message="Do you really want to exit?"):     
                self.window_2.destroy()

    def name_table(self):
        new_window = Toplevel()
        new_window.iconbitmap('463407-200.ico')
        new_window.title("Queue table")
        new_window.geometry('1270x250')
        self.table = ttk.Treeview(new_window, columns=('col1', 'col2', 'col3', 'col4'), show='headings')
        self.table.grid(row=1, column=1, padx = 20, sticky=W)
        self.table.column('col1', width=300)
        self.table.column('col2', width=300)
        self.table.column('col3', width=300)
        self.table.column('col4', width=300)
        self.table.heading('col1', text="Roller Coaster Train")
        self.table.heading('col2', text="Tornado")
        self.table.heading('col3', text="Thunder Bird")
        self.table.heading('col4', text="Super Splash")

        with open('Num_Roller_Coaster_Train.txt', 'r') as file:
            lines_1 = file.readlines()
        lines_1_1 = [line.strip() for line in lines_1]
        queue_ro = self.count_names(lines_1_1)

        with open('Num_Tornado.txt', 'r') as file:
            lines_2 = file.readlines()
        lines_2_2 = [line.strip() for line in lines_2]
        queue_to = self.count_names(lines_2_2)

        with open('Num_Thunder_Bird.txt', 'r') as file:
            lines_3 = file.readlines()
        lines_3_3 = [line.strip() for line in lines_3]
        queue_th = self.count_names(lines_3_3)

        with open('Num_Super_Splash.txt', 'r') as file:
            lines_4 = file.readlines()
        lines_4_4 = [line.strip() for line in lines_4]
        queue_su = self.count_names(lines_4_4)

        max_length = max(len(queue_ro), len(queue_to), len(queue_th), len(queue_su))
        new_list_1 = [item if item[0] is not None else ('', '') for item in queue_ro] + [('', '')] * (max_length - len(queue_ro))
        new_list_2 = [item if item[0] is not None else ('', '') for item in queue_to] + [('', '')] * (max_length - len(queue_to))
        new_list_3 = [item if item[0] is not None else ('', '') for item in queue_th] + [('', '')] * (max_length - len(queue_th))
        new_list_4 = [item if item[0] is not None else ('', '') for item in queue_su] + [('', '')] * (max_length - len(queue_su))

        result = [item for sublist in zip(new_list_1, new_list_2, new_list_3, new_list_4) for item in sublist]

        count = 1
        for tree in range(0, len(result), 4):
            chunk = result[tree:tree + 4]
            self.table.insert('', 'end', values=(
                f"{count}. {chunk[0][0]} {chunk[0][1]} person." if chunk[0][0] or chunk[0][1] else '',
                f"{count}. {chunk[1][0]} {chunk[1][1]} person." if chunk[1][0] or chunk[1][1] else '',
                f"{count}. {chunk[2][0]} {chunk[2][1]} person." if chunk[2][0] or chunk[2][1] else '',
                f"{count}. {chunk[3][0]} {chunk[3][1]} person." if chunk[3][0] or chunk[3][1] else ''
            ))
            count += 1
        
        scrollbar = ttk.Scrollbar(new_window, orient=VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky='ns')



    def settimer(self, place):
        if place == 1:
            self.new_window_1 = Toplevel()
            self.new_window_1.configure(bg='#00dbd5')
            self.new_window_1.title("Set time Roller Coaster Train")
            self.new_window_1.protocol("WM_DELETE_WINDOW", lambda:self.on_closing(1))
            self.new_window_1.iconbitmap('463407-200.ico')

            self.text1 = Label(self.new_window_1, text="HOURS", font=("Candara",10,'bold'), bg='#00dbd5')
            self.text2 = Label(self.new_window_1, text="MINUTES", font=("Candara",10,'bold'), bg='#00dbd5')
            self.text3 = Label(self.new_window_1, text="SECONDS", font=("Candara",10,'bold'), bg='#00dbd5')
            self.text1.grid(row=0,column=1, padx=10, pady=2)
            self.text2.grid(row=0,column=2, padx=10, pady=2)
            self.text3.grid(row=0,column=3, padx=10, pady=2)

            self.hour_1=StringVar()
            self.minute_1=StringVar()
            self.second_1=StringVar()
            # Use of Entry class to take input from the user
            self.hourEntry1= Entry(self.new_window_1, width=10, font=('BrowalliaUPC',18,'normal'),
                            textvariable=self.hour_1)
            self.hourEntry1.grid(row=1,column=1, padx=10, pady=2)
            
            self.minuteEntry1= Entry(self.new_window_1, width=10, font=('BrowalliaUPC',18,'normal'),
                            textvariable=self.minute_1)
            self.minuteEntry1.grid(row=1,column=2, padx=10, pady=2)
            
            self.secondEntry1= Entry(self.new_window_1, width=10, font=('BrowalliaUPC',18,'normal'),
                            textvariable=self.second_1)
            self.secondEntry1.grid(row=1,column=3, padx=10, pady=2)

            self.btn1 = Button(self.new_window_1, text='Set Time Countdown', bd='5', command= lambda: self.confirm_button_click(1), bg='#ffcecd', font= ('Elephant', 10, 'italic'))
            self.btn1.grid(row=2,column=1,pady=10,columnspan=3)

            self.new_window_1.bind('<Return>', self.count_time_call_self1)

        if place == 2:
            self.new_window_2 = Toplevel()
            self.new_window_2.title("Set time Tornado")
            self.new_window_2.configure(bg='#00dbd5')
            self.new_window_2.protocol("WM_DELETE_WINDOW", lambda:self.on_closing(2))
            self.new_window_2.iconbitmap('463407-200.ico')

            self.text1 = Label(self.new_window_2, text="HOURS", font=("Candara",10,'bold'), bg='#00dbd5')
            self.text2 = Label(self.new_window_2, text="MINUTES", font=("Candara",10,'bold'), bg='#00dbd5')
            self.text3 = Label(self.new_window_2, text="SECONDS", font=("Candara",10,'bold'), bg='#00dbd5')
            self.text1.grid(row=0,column=1, padx=10, pady=2)
            self.text2.grid(row=0,column=2, padx=10, pady=2)
            self.text3.grid(row=0,column=3, padx=10, pady=2)

            self.hour_2=StringVar()
            self.minute_2=StringVar()
            self.second_2=StringVar()
            
            self.hourEntry2= Entry(self.new_window_2, width=10, font=('BrowalliaUPC',18,'normal'),
                            textvariable=self.hour_2)
            self.hourEntry2.grid(row=1,column=1, padx=10, pady=2)
            
            self.minuteEntry2= Entry(self.new_window_2, width=10, font=('BrowalliaUPC',18,'normal'),
                            textvariable=self.minute_2)
            self.minuteEntry2.grid(row=1,column=2, padx=10, pady=2)
            
            self.secondEntry2= Entry(self.new_window_2, width=10, font=('BrowalliaUPC',18,'normal'),
                            textvariable=self.second_2)
            self.secondEntry2.grid(row=1,column=3, padx=10, pady=2)

            self.btn2 = Button(self.new_window_2, text='Set Time Countdown', bd='5', command= lambda: self.confirm_button_click(2), bg='#ffcecd', font= ('Elephant', 10, 'italic')
                )
            self.btn2.grid(row=2,column=1,pady=10,columnspan = 3)

            self.new_window_2.bind('<Return>', self.count_time_call_self2)

        if place == 3:
            self.new_window_3 = Toplevel()
            self.new_window_3.title("Set time Thunder Bird")
            self.new_window_3.configure(bg='#00dbd5')
            self.new_window_3.protocol("WM_DELETE_WINDOW", lambda:self.on_closing(3))
            self.new_window_3.iconbitmap('463407-200.ico')

            self.text1 = Label(self.new_window_3, text="HOURS", font=("Candara",10,'bold'), bg='#00dbd5')
            self.text2 = Label(self.new_window_3, text="MINUTES", font=("Candara",10,'bold'), bg='#00dbd5')
            self.text3 = Label(self.new_window_3, text="SECONDS", font=("Candara",10,'bold'), bg='#00dbd5')
            self.text1.grid(row=0,column=1, padx=10, pady=2)
            self.text2.grid(row=0,column=2, padx=10, pady=2)
            self.text3.grid(row=0,column=3, padx=10, pady=2)

            self.hour_3=StringVar()
            self.minute_3=StringVar()
            self.second_3=StringVar()
            
            self.hourEntry3= Entry(self.new_window_3, width=10, font=('BrowalliaUPC',18,'normal'),
                            textvariable=self.hour_3)
            self.hourEntry3.grid(row=1,column=1, padx=10, pady=2)
            
            self.minuteEntry3= Entry(self.new_window_3, width=10, font=('BrowalliaUPC',18,'normal'),
                            textvariable=self.minute_3)
            self.minuteEntry3.grid(row=1,column=2, padx=10, pady=2)
            
            self.secondEntry3= Entry(self.new_window_3, width=10, font=('BrowalliaUPC',18,'normal'),
                            textvariable=self.second_3)
            self.secondEntry3.grid(row=1,column=3, padx=10, pady=2)

            self.btn3 = Button(self.new_window_3, text='Set Time Countdown', bd='5', command= lambda: self.confirm_button_click(3), bg='#ffcecd', font= ('Elephant', 10, 'italic'))
            self.btn3.grid(row=2,column=1,pady=10, columnspan=3)

            self.new_window_3.bind('<Return>', self.count_time_call_self3)

        if place == 4:
            self.new_window_4 = Toplevel()
            self.new_window_4.title("Set time Super Splash")
            self.new_window_4.configure(bg='#00dbd5')
            self.new_window_4.protocol("WM_DELETE_WINDOW", lambda:self.on_closing(4))
            self.new_window_4.iconbitmap('463407-200.ico')

            self.text1 = Label(self.new_window_4, text="HOURS", font=("Candara",10,'bold'), bg='#00dbd5')
            self.text2 = Label(self.new_window_4, text="MINUTES", font=("Candara",10,'bold'), bg='#00dbd5')
            self.text3 = Label(self.new_window_4, text="SECONDS", font=("Candara",10,'bold'), bg='#00dbd5')
            self.text1.grid(row=0,column=1, padx=10, pady=2)
            self.text2.grid(row=0,column=2, padx=10, pady=2)
            self.text3.grid(row=0,column=3, padx=10, pady=2)

            self.hour_4=StringVar()
            self.minute_4=StringVar()
            self.second_4=StringVar()

            self.hourEntry4= Entry(self.new_window_4, width=10, font=('BrowalliaUPC',18,'normal'),
                            textvariable=self.hour_4)
            self.hourEntry4.grid(row=1,column=1, padx=10, pady=2)
            
            self.minuteEntry4= Entry(self.new_window_4, width=10, font=('BrowalliaUPC',18,'normal'),
                            textvariable=self.minute_4)
            self.minuteEntry4.grid(row=1,column=2, padx=10, pady=2)
            
            self.secondEntry4= Entry(self.new_window_4, width=10, font=('BrowalliaUPC',18,'normal'),
                            textvariable=self.second_4)
            self.secondEntry4.grid(row=1,column=3, padx=10, pady=2)

            self.btn4 = Button(self.new_window_4, text='Set Time Countdown', bd='5', command= lambda: self.confirm_button_click(4), bg='#ffcecd', font= ('Elephant', 10, 'italic'))
            self.btn4.grid(row=2,column=1,pady=10, columnspan=3)

            self.new_window_4.bind('<Return>', self.count_time_call_self4)

    def confirm_button_click(self, place):
        if place == 1:
            confirmed = tkinter.messagebox.askyesno("Confirm", "Do you want to start countdown?")
            if confirmed:
                self.count_time(1)

        if place == 2:
            confirmed = tkinter.messagebox.askyesno("Confirm", "Do you want to start countdown?")
            if confirmed:
                self.count_time(2)

        if place == 3:
            confirmed = tkinter.messagebox.askyesno("Confirm", "Do you want to start countdown?")
            if confirmed:
                self.count_time(3)

        if place == 4:
            confirmed = tkinter.messagebox.askyesno("Confirm", "Do you want to start countdown?")
            if confirmed:
                self.count_time(4)

    def count_time_call_self1(self, event):
        self.confirm_button_click(1)

    def count_time_call_self2(self, event):
        self.confirm_button_click(2)

    def count_time_call_self3(self, event):
        self.confirm_button_click(3)

    def count_time_call_self4(self, event):
        self.confirm_button_click(4)

    def count_time(self, place):
        if place == 1:
            try:
                if self.hourEntry1.get() == '':
                    self.hour_1.set('0')
                if self.minuteEntry1.get() == '':
                    self.minute_1.set('0')
                if self.secondEntry1.get() == '':
                    self.second_1.set('0')
                hours = int(self.hourEntry1.get()) * 3600
                minutes = int(self.minuteEntry1.get()) * 60
                seconds = int(self.secondEntry1.get())
                real_sec = hours + minutes + seconds
                self.countdown(real_sec, 1)
                self.new_window_1.destroy()
            except ValueError:
                tkinter.messagebox.showerror("Error", "Please enter a number")

        if place == 2:
            try:
                if self.hourEntry2.get() == '':
                    self.hour_2.set('0')
                if self.minuteEntry2.get() == '':
                    self.minute_2.set('0')
                if self.secondEntry2.get() == '':
                    self.second_2.set('0')
                hours = int(self.hourEntry2.get()) * 3600
                minutes = int(self.minuteEntry2.get()) * 60
                seconds = int(self.secondEntry2.get())
                real_sec = hours + minutes + seconds
                self.countdown(real_sec, 2)
                self.new_window_2.destroy()
            except ValueError:
                tkinter.messagebox.showerror("Error", "Please enter a number")

        if place == 3:
            try:
                if self.hourEntry3.get() == '':
                    self.hour_3.set('0')
                if self.minuteEntry3.get() == '':
                    self.minute_3.set('0')
                if self.secondEntry3.get() == '':
                    self.second_3.set('0')
                hours = int(self.hourEntry3.get()) * 3600
                minutes = int(self.minuteEntry3.get()) * 60
                seconds = int(self.secondEntry3.get())
                real_sec = hours + minutes + seconds
                self.countdown(real_sec, 3)
                self.new_window_3.destroy()
            except ValueError:
                tkinter.messagebox.showerror("Error", "Please enter a number")

        if place == 4:
            try:
                if self.hourEntry4.get() == '':
                    self.hour_4.set('0')
                if self.minuteEntry4.get() == '':
                    self.minute_4.set('0')
                if self.secondEntry4.get() == '':
                    self.second_4.set('0')
                hours = int(self.hourEntry4.get()) * 3600
                minutes = int(self.minuteEntry4.get()) * 60
                seconds = int(self.secondEntry4.get())
                real_sec = hours + minutes + seconds
                self.countdown(real_sec, 4)
                self.new_window_4.destroy()
            except ValueError:
                tkinter.messagebox.showerror("Error", "Please enter a number")
        
    def on_closing(self, place):
        if place == 1:
            if tkinter.messagebox.askyesno(title="Exit?", message="Do you really want to exit?"):     
                self.new_window_1.destroy()

        if place == 2:
            if tkinter.messagebox.askyesno(title="Exit?", message="Do you really want to exit?"):     
                self.new_window_2.destroy()

        if place == 3:
            if tkinter.messagebox.askyesno(title="Exit?", message="Do you really want to exit?"):     
                self.new_window_3.destroy()

        if place == 4:
            if tkinter.messagebox.askyesno(title="Exit?", message="Do you really want to exit?"):     
                self.new_window_4.destroy()


    def delete_name(self, place):
        if place == 1:
            element = self.entry_1_delete.get()
            count = 0
            for i in range(0, self.first_machine.get_size_element()):
                if self.first_machine.queue[i][0] == element:
                    count += 1
            for n in range(count):
                self.delete_name_in_queue(self.first_machine, element)
                self.set_laa1_text(str(self.first_machine.get_size_element()))
            # Read the content of the file
            with open('Num_Roller_Coaster_Train.txt', 'r') as file:
                lines = file.readlines()

            # Modify the content by removing the specified element
            lines = [line for line in lines if line.strip() != element]

            # Write the modified content back to the file
            with open('Num_Roller_Coaster_Train.txt', 'w') as file:
                file.writelines(lines)

        if place == 2:
            element = self.entry_2_delete.get()
            count = 0
            for i in range(self.second_machine.get_size_element()):
                if self.second_machine.queue[i][0] == element:
                    count += 1
            for n in range(count):
                self.delete_name_in_queue(self.second_machine, element)
                self.set_laa2_text(str(self.second_machine.get_size_element()))
            # Read the content of the file
            with open('Num_Tornado.txt', 'r') as file:
                lines = file.readlines()

            # Modify the content by removing the specified element
            lines = [line for line in lines if line.strip() != element]

            # Write the modified content back to the file
            with open('Num_Tornado.txt', 'w') as file:
                file.writelines(lines)

        if place == 3:
            element = self.entry_3_delete.get()
            count = 0
            for i in range(self.third_machine.get_size_element()):
                if self.third_machine.queue[i][0] == element:
                    count += 1
            for n in range(count):
                self.delete_name_in_queue(self.third_machine, element)
                self.set_laa3_text(str(self.third_machine.get_size_element()))
            # Read the content of the file
            with open('Num_Thunder_Bird.txt', 'r') as file:
                lines = file.readlines()

            # Modify the content by removing the specified element
            lines = [line for line in lines if line.strip() != element]

            # Write the modified content back to the file
            with open('Num_Thunder_Bird.txt', 'w') as file:
                file.writelines(lines)

        if place == 4:
            element = self.entry_4_delete.get()
            count = 0
            for i in range(self.fouth_machine.get_size_element()):
                if self.fouth_machine.queue[i][0] == element:
                    count += 1
            for n in range(count):
                self.delete_name_in_queue(self.fouth_machine, element)
                self.set_laa4_text(str(self.fouth_machine.get_size_element()))
            # Read the content of the file
            with open('Num_Super_Splash.txt', 'r') as file:
                lines = file.readlines()

            # Modify the content by removing the specified element
            lines = [line for line in lines if line.strip() != element]

            # Write the modified content back to the file
            with open('Num_Super_Splash.txt', 'w') as file:
                file.writelines(lines)

    def delete_name_in_queue(self, queue, element):
        if queue.front == -1:
            return False

        # Find the index of the element to delete
        index = queue.front
        while queue.queue[index][0] != element:
            index = (index + 1) % queue.size
            if index == queue.front:
                # Element not found
                return False
            
        queue.queue.remove(queue.queue[index])
        queue.queue.append(None)
        
        # Update head and rear pointers
        if queue.front == queue.rear:
            queue.front = -1
            queue.rear = -1
        else:
            queue.rear = (queue.rear - 1) % queue.size
        
        return True

    def set_laa1_text(self, laa1):
        self.laa1.config(text=laa1)

    def set_laa2_text(self, laa2):
        self.laa2.config(text=laa2)

    def set_laa3_text(self, laa3):
        self.laa3.config(text=laa3)
        
    def set_laa4_text(self, laa4):
        self.laa4.config(text=laa4)

    def command(self, place):
        if place == 1:
            Popup_Roller_Coaster_Train(self)
        if place == 2:
            Popup_Tornado(self)
        if place == 3:
            Popup_Thunder_Bird(self)
        if place == 4:
            Popup_Super_Splash(self)

    def time(self):
        string = strftime('%H:%M:%S %p')
        self.time_earth.config(text=string)
        self.time_earth.after(1000, self.time)

    def countdown(self, count, place):
        if place == 1:
            hour = int(count/3600)
            minute = int(count/60)%60
            sec = count % 60

            # change text in label        
            self.label_countdown_1['text'] = f"Ends in: {hour:02}:{minute:02}:{sec:02}"

            if count > 0:
                # call countdown again after 1000ms (1s)
                self.window_2.after(1000, self.countdown, count-1, 1)

            if count == 0:

                if self.first_machine.get_size_element()-20 >= 0:
                    self.set_laa1_text(str(self.first_machine.get_size_element()-20))
                else:
                    self.set_laa1_text('0')

                if self.first_machine.get_size_element() != 0:
                    x=[]
                    for i in range(20):
                        p = self.first_machine.dequeue()
                        if p != None:
                            x.append(p)


                    with open('Num_Roller_Coaster_Train.txt', 'r') as f:
                        lines = f.readlines()[20:]  # skip the first 20 lines

                    with open('Num_Roller_Coaster_Train.txt', 'w') as f:
                        f.writelines(lines)

                    
                    count_num_people_list = []
                    for j in x:
                        count_num_people_list.append(j[0])
                        
                    count_people = self.count_names(count_num_people_list)
                    count_n = 1
                    str1 = ""
                    for i in range(len(count_people)):
                                str1 += f"{count_n}. {count_people[i][0]} {count_people[i][1]} people.\n"
                                count_n += 1

                    tkinter.messagebox.showinfo("Roller Coaster Train", f"{str1} \nplease stand by.")

        if place == 2:
            hour = int(count/3600)
            minute = int(count/60)%60
            sec = count % 60

            # change text in label        
            self.label_countdown_2['text'] = f"Ends in: {hour:02}:{minute:02}:{sec:02}"

            if count > 0:
                # call countdown again after 1000ms (1s)
                self.window_2.after(1000, self.countdown, count-1, 2)

            if count == 0:

                if self.second_machine.get_size_element()-20 >= 0:
                    self.set_laa2_text(str(self.second_machine.get_size_element()-20))
                else:
                    self.set_laa2_text('0')

                if self.second_machine.get_size_element() != 0:
                    x=[]
                    for i in range(20):
                        p = self.second_machine.dequeue()
                        if p != None:
                            x.append(p)


                    with open('Num_Tornado.txt', 'r') as f:
                        lines = f.readlines()[20:]  # skip the first 20 lines

                    with open('Num_Tornado.txt', 'w') as f:
                        f.writelines(lines)
                    
                    count_num_people_list = []
                    for j in x:
                        count_num_people_list.append(j[0])
                        
                    count_people = self.count_names(count_num_people_list)
                    count_n = 1
                    str1 = ""
                    for i in range(len(count_people)):
                                str1 += f"{count_n}. {count_people[i][0]} {count_people[i][1]} people.\n"
                                count_n += 1

                    tkinter.messagebox.showinfo("Tornado", f"{str1} \nplease stand by.")

        if place == 3:
            hour = int(count/3600)
            minute = int(count/60)%60
            sec = count % 60

            # change text in label        
            self.label_countdown_3['text'] = f"Ends in: {hour:02}:{minute:02}:{sec:02}"

            if count > 0:
                # call countdown again after 1000ms (1s)
                self.window_2.after(1000, self.countdown, count-1, 3)

            if count == 0:

                if self.third_machine.get_size_element()-8 >= 0:
                    self.set_laa3_text(str(self.third_machine.get_size_element()-8))
                else:
                    self.set_laa3_text('0')

                
                if self.third_machine.get_size_element() != 0:
                    x=[]
                    for i in range(8):
                        p = self.third_machine.dequeue()
                        if p != None:
                            x.append(p)


                    with open('Num_Thunder_Bird.txt', 'r') as f:
                        lines = f.readlines()[8:]  # skip the first 20 lines

                    with open('Num_Thunder_Bird.txt', 'w') as f:
                        f.writelines(lines)
                    
                    count_num_people_list = []
                    for j in x:
                        count_num_people_list.append(j[0])
                        
                    count_people = self.count_names(count_num_people_list)
                    count_n = 1
                    str1 = ""
                    for i in range(len(count_people)):
                                str1 += f"{count_n}. {count_people[i][0]} {count_people[i][1]} people.\n"
                                count_n += 1

                    tkinter.messagebox.showinfo("Thunder Bird", f"{str1} \nplease stand by.")

        if place == 4:
            hour = int(count/3600)
            minute = int(count/60)%60
            sec = count % 60

            # change text in label        
            self.label_countdown_4['text'] = f"Ends in: {hour:02}:{minute:02}:{sec:02}"

            if count > 0:
                # call countdown again after 1000ms (1s)
                self.window_2.after(1000, self.countdown, count-1, 4)

            if count == 0:
                
                if self.fouth_machine.get_size_element()-12 >= 0:
                    self.set_laa4_text(str(self.fouth_machine.get_size_element()-12))
                else:
                    self.set_laa4_text('0')

                if self.fouth_machine.get_size_element() != 0:
                    x=[]
                    for i in range(12):
                        p = self.fouth_machine.dequeue()
                        if p != None:
                            x.append(p)
                        

                    with open('Num_Super_Splash.txt', 'r') as f:
                        lines = f.readlines()[12:]  # skip the first 20 lines

                    with open('Num_Super_Splash.txt', 'w') as f:
                        f.writelines(lines)
                    
                    count_num_people_list = []
                    for j in x:
                        count_num_people_list.append(j[0])
                        
                    count_people = self.count_names(count_num_people_list)
                    count_n = 1
                    str1 = ""
                    for i in range(len(count_people)):
                                str1 += f"{count_n}. {count_people[i][0]} {count_people[i][1]} people.\n"
                                count_n += 1

                    tkinter.messagebox.showinfo("Super Splash", f"{str1} \nplease stand by.")

    def count_names(self, list_name):
        counts = []
        previous_name = None
        current_name = None
        current_count = 0

        for line in list_name:
            name = line.strip()

            if current_name is None:
                current_name = name
                current_count = 1
            elif name == current_name:
                current_count += 1
            else:
                counts.append((current_name, current_count))
                previous_name = current_name
                current_name = name
                current_count = 1

        counts.append((current_name, current_count))

        return counts
    
    def count_back_up_data(self, file_path):
        counts = []

        with open(file_path, 'r') as file:
            previous_name = None
            current_name = None
            current_count = 0

            for line in file:
                name = line.strip()

                if current_name is None:
                    current_name = name
                    current_count = 1
                elif name == current_name:
                    current_count += 1
                else:
                    counts.append((current_name, current_count))
                    previous_name = current_name
                    current_name = name
                    current_count = 1

            counts.append((current_name, current_count))

        queue = []
        for name in counts:
            if name[1] >= 2:
                for amount in range(name[1]):
                    queue.append(name)
            if name[1] == 1:
                queue.append(name)

        return queue

# The above class represents a login page for the first page of a website.
class first_page_login:
    def __init__(self):
            
            self.window = Tk()
            self.window.title("My Dream World")
            self.window.configure(bg='lightpink')
            self.window.iconbitmap('463407-200.ico')
            self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
            
            self.image = PhotoImage(file='logo-removebg-preview.png')

            self.labe = Label(self.window,text='', padx = 140, pady = 80, bg='lightpink')
            self.labe.grid(row=1, column=2)

            self.label_1 = Label(self.window, image=self.image, padx = 140, pady = 5, bg='lightpink')
            self.label_1.grid(row=5, column=2)

            self.label_2 = Label(self.window, text= "Make a Reservation\nTheme Park", font= ("Segoe UI Black", 20, "bold"), padx = 140, pady = 5, bg='lightpink')
            self.label_2.grid(column=2, row=6)

            self.button1 = Button(self.window, text= "Click Start", width = 12, command= self.make, font= ("Viner Hand ITC", 10, 'italic'), padx = 140, pady = 10, fg = '#864d9c', bd = '5')
            self.button1.grid(column=2, row=7)
            
            self.label_4 = Label(self.window, text= "Please Enjoy", font= ("YouYuan", 12, "bold"), padx = 140, pady = 10, bg='lightpink', fg = '#006db1')
            self.label_4.grid(column=2, row=8)
            self.label_3 = Label(self.window, text= "- - -  \"Your Dream World\"  - - -", font= ("STENCIL", 14, "bold"), padx = 140, bg='lightpink', fg = '#864d9c')
            self.label_3.grid(column=2, row=9)
            self.label_11 = Label(self.window, text= "Open : 08:00:00 AM", font= ("YouYuan", 10, "bold"), padx = 140, pady = 10, bg='lightpink', fg = '#9a6db1')
            self.label_11.grid(column=2, row=10)
            self.label_12 = Label(self.window, text= "Close : 18:00:00 PM", font= ("YouYuan", 10, "bold"), padx = 140, bg='lightpink', fg = '#9a6db1')
            self.label_12.grid(column=2, row=11)

            self.labe0 = Label(self.window,text='',pady = 80, bg='lightpink')
            self.labe0.grid(row=12, column=2)

            self.window.bind('<Return>', self.make_press)

            self.window.mainloop()
    
    def on_closing(self):
        if tkinter.messagebox.askyesno(title="Exit?", message="Do you really want to exit?"):     
                self.window.destroy()

    def make_press(self, event):
        self.make()

    def make(self):
        self.window.destroy()
        Project_prototypes_main_page()

# The class is used to create a popup self.window for making a reservation.
class Popup_make_reservasion_info_main:
    def __init__(self):
        self.pop = Toplevel()
        self.pop.iconbitmap('463407-200.ico')
        self.pop.configure(bg='lightpink')

    def name(self):
        self.label_1 = Label(self.pop, text= "Firstname:", font= ("Calibri", 12, 'bold'), bg='lightpink')
        self.label_1.grid(row=1,column=1, sticky=W, pady=10, padx=10)

    def surname(self):
        self.label_2 = Label(self.pop, text= "Surname:", font= ("Calibri", 12, 'bold'), bg='lightpink')
        self.label_2.grid(row=2,column=1, sticky=W, pady=10, padx=10)

    def description(self):
        self.label_3 = Label(self.pop, text= "Make a reservation:", font= ("Calibri", 12, 'bold'), bg='lightpink')
        self.label_3.grid(row=4,column=1, sticky=W, pady=10, padx=10)

    def amount_of_people(self):
        self.label_34 = Label(self.pop, text= "Amount of people:", font= ("Calibri", 12, 'bold'), bg='lightpink')
        self.label_34.grid(row=3,column=1, sticky=W, pady=10, padx=10)

# The class `Popup_Roller_Coaster_Train` is a subclass of `Popup_make_reservasion_info_main` and is
# used for making reservations for a roller coaster train.
class Popup_Roller_Coaster_Train(Popup_make_reservasion_info_main):
    def __init__(self, main_page_instance):
        super().__init__()

        self.pop.title("Roller Coaster")

        self.name_var_1 = StringVar()
        self.sur_var_1 = StringVar()
        self.amount_1 = IntVar()
        self.pop.bind('<Return>', self.make_press)

        self.main_page_instance = main_page_instance

        super().name()
        self.entry_1 = Entry(self.pop, textvariable= self.name_var_1, font=('YouYuan',10,'normal'))
        self.entry_1.grid(row=1,column=2)

        super().surname()
        self.entry_2 = Entry(self.pop, textvariable= self.sur_var_1, font=('YouYuan',10,'normal'))
        self.entry_2.grid(row=2,column=2)
        
        super().amount_of_people()
        self.spinbox_people_1 = ttk.Spinbox(self.pop, textvariable= self.amount_1, from_ = 1, to = 20, width = 5, wrap =True, font=('YouYuan',10,'normal'))
        self.spinbox_people_1.grid(row=3,column=2,padx=6, sticky=W)
    
        super().description()
        self.btn_1 = Button(self.pop, text = "Confirm", font= ("Elephant", 8, 'italic'), width = 17, command=self.add_queue_1)
        self.btn_1.grid(row=4, column = 2, padx=5, pady=5)

    def make_press(self, event):
        self.add_queue_1()

    def get_data_1(self):
        self.full_name = self.entry_1.get().strip() +' '+ self.entry_2.get().strip()
        tup = (self.full_name, self.spinbox_people_1.get())
        return tup

    def add_queue_1(self):
        try:
            data = self.get_data_1()

            if len(self.entry_1.get()) == 0 and len(self.entry_2.get()) == 0:
                raise TypeError("Please check your Name Surname and amount.")
            
            elif len(self.entry_1.get()) == 0:
                raise NameError("Please check your Name.")
            
            elif len(self.entry_2.get()) == 0:
                raise SyntaxError("Please check your Surname.")
            
            else:
                data_file = open("Num_Roller_Coaster_Train.txt", 'a')
                for i in range(int(self.spinbox_people_1.get())):
                    self.main_page_instance.first_machine.enqueue(data)
                    
                    if self.main_page_instance.laa1.cget("text"):
                        data_file.write(self.entry_1.get().strip()  +' '+ self.entry_2.get().strip() +"\n")
                    self.main_page_instance.set_laa1_text(self.main_page_instance.first_machine.get_size_element())
                
                data_file.close()
                tkinter.messagebox.showinfo("", "Yours reservation is successfully")

        except ValueError:
            tkinter.messagebox.showerror("", "Please check your entered amount of people.")

        except NameError as error:
            tkinter.messagebox.showerror("", f"{error}")

        except SyntaxError as error:
            tkinter.messagebox.showerror("", f"{error}")
        
        except TypeError as error:
            tkinter.messagebox.showerror("", f"{error}")
            
        self.pop.destroy()

# The class Popup_Tornado is a subclass of the class Popup_make_reservasion_info_main.
class Popup_Tornado(Popup_make_reservasion_info_main):
    def __init__(self, main_page_instance):
        super().__init__()

        self.pop.title("Tornado")

        self.name_var_2 = StringVar()
        self.sur_var_2 = StringVar()
        self.amount_2 = StringVar()
        self.pop.bind('<Return>', self.make_press)

        self.main_page_instance = main_page_instance

        super().name()
        self.entry_1 = Entry(self.pop, textvariable= self.name_var_2, font=('YouYuan',10,'normal'))
        self.entry_1.grid(row=1,column=2)

        super().surname()
        self.entry_2 = Entry(self.pop, textvariable= self.sur_var_2, font=('YouYuan',10,'normal'))
        self.entry_2.grid(row=2,column=2)
        
        super().amount_of_people()
        self.spinbox_people_2 = ttk.Spinbox(self.pop, textvariable= self.amount_2, from_ = 1, to = 20, width = 5, wrap =True, font=('YouYuan',10,'normal'))
        self.spinbox_people_2.grid(row=3,column=2,padx=6, sticky=W)

        super().description()
        self.btn_2 = Button(self.pop, text = "Confirm", font= ("Elephant", 8, 'italic'), width = 17, command=self.add_queue_2)
        self.btn_2.grid(row=4, column = 2, padx=5, pady=5)

    def make_press(self, event):
        self.add_queue_2()
        
    def get_data_2(self):
        self.full_name = self.entry_1.get().strip() +' '+ self.entry_2.get().strip()
        tup = (self.full_name, self.spinbox_people_2.get())

        return tup

    def add_queue_2(self):
        try:
            data = self.get_data_2()

            if len(self.entry_1.get()) == 0 and len(self.entry_2.get()) == 0:
                raise TypeError("Please check your Name Surname and amount.")
            
            elif len(self.entry_1.get()) == 0:
                raise NameError("Please check your Name.")
            
            elif len(self.entry_2.get()) == 0:
                raise SyntaxError("Please check your Surname.")
            
            else:
                data_file = open("Num_Tornado.txt", 'a')
                for i in range(int(self.spinbox_people_2.get())):
                    self.main_page_instance.second_machine.enqueue(data)

                    if self.main_page_instance.laa2.cget("text"):
                        data_file.write(self.entry_1.get().strip() +' '+ self.entry_2.get().strip()+"\n")
                    self.main_page_instance.set_laa2_text(self.main_page_instance.second_machine.get_size_element())

                data_file.close()
                tkinter.messagebox.showinfo("", "Yours reservation is successfully")
                
        except ValueError:
            tkinter.messagebox.showerror("", "Please check your entered amount of people.")

        except NameError as error:
            tkinter.messagebox.showerror("", f"{error}")

        except SyntaxError as error:
            tkinter.messagebox.showerror("", f"{error}")
        
        except TypeError as error:
            tkinter.messagebox.showerror("", f"{error}")

        self.pop.destroy()


# The class `Popup_Thunder_Bird` is a subclass of `Popup_make_reservasion_info_main` and likely
# contains additional functionality related to making a reservation.
class Popup_Thunder_Bird(Popup_make_reservasion_info_main):
    def __init__(self, main_page_instance):
        super().__init__()

        self.pop.title("Thunder Bird")

        self.name_var_3 = StringVar()
        self.sur_var_3 = StringVar()
        self.amount_3 = IntVar()
        self.pop.bind('<Return>', self.make_press)

        self.main_page_instance = main_page_instance

        super().name()
        self.entry_1 = Entry(self.pop, textvariable= self.name_var_3, font=('YouYuan',10,'normal'))
        self.entry_1.grid(row=1,column=2)

        super().surname()
        self.entry_2 = Entry(self.pop, textvariable= self.sur_var_3, font=('YouYuan',10,'normal'))
        self.entry_2.grid(row=2,column=2)
        
        super().amount_of_people()
        self.spinbox_people_3 = ttk.Spinbox(self.pop, textvariable= self.amount_3, from_ = 1, to = 8, width = 5, wrap =True, font=('YouYuan',10,'normal'))
        self.spinbox_people_3.grid(row=3,column=2,padx=6, sticky=W)

        super().description()
        self.btn_3 = Button(self.pop, text = "Confirm", font= ("Elephant", 8, 'italic'), width = 17, command=self.add_queue_3)
        self.btn_3.grid(row=4, column = 2, padx=5, pady=5)

    def make_press(self, event):
        self.add_queue_3()

    def get_data_3(self):
        self.full_name = self.entry_1.get().strip() +' '+ self.entry_2.get().strip()
        tup = (self.full_name, self.spinbox_people_3.get())
        return tup
    
    def add_queue_3(self):
        try:
            data = self.get_data_3()

            if len(self.entry_1.get()) == 0 and len(self.entry_2.get()) == 0:
                raise TypeError("Please check your Name Surname and amount.")
            
            elif len(self.entry_1.get()) == 0:
                raise NameError("Please check your Name.")
            
            elif len(self.entry_2.get()) == 0:
                raise SyntaxError("Please check your Surname.")
            
            else:
                data_file = open("Num_Thunder_Bird.txt", 'a')
                for i in range(int(self.spinbox_people_3.get())):
                    self.main_page_instance.third_machine.enqueue(data)

                    if self.main_page_instance.laa3.cget("text"):
                        data_file.write(self.entry_1.get().strip() +' '+ self.entry_2.get().strip()+"\n")
                    self.main_page_instance.set_laa3_text(self.main_page_instance.third_machine.get_size_element())
                
                data_file.close()
                tkinter.messagebox.showinfo("", "Yours reservation is successfully")
        
        except ValueError:
            tkinter.messagebox.showerror("", "Please check your entered amount of people.")

        except NameError as error:
            tkinter.messagebox.showerror("", f"{error}")

        except SyntaxError as error:
            tkinter.messagebox.showerror("", f"{error}")
        
        except TypeError as error:
            tkinter.messagebox.showerror("", f"{error}")

        self.pop.destroy()


# The class `Popup_Super_Splash` is a subclass of `Popup_make_reservasion_info_main` and is used for
# creating a popup self.window for making reservations.
class Popup_Super_Splash(Popup_make_reservasion_info_main):
    def __init__(self, main_page_instance):
        super().__init__()

        self.pop.title("Super Splash")

        self.name_var_4 = StringVar()
        self.sur_var_4 = StringVar()
        self.amount_4 = IntVar()
        self.pop.bind('<Return>', self.make_press)

        self.main_page_instance = main_page_instance

        super().name()
        self.entry_1 = Entry(self.pop, textvariable= self.name_var_4, font=('YouYuan',10,'normal'))
        self.entry_1.grid(row=1,column=2)

        super().surname()
        self.entry_2 = Entry(self.pop, textvariable= self.sur_var_4, font=('YouYuan',10,'normal'))
        self.entry_2.grid(row=2,column=2)
        
        super().amount_of_people()
        self.spinbox_people_4 = ttk.Spinbox(self.pop, textvariable= self.amount_4, from_ = 1, to = 12, width = 5, wrap =True, font=('YouYuan',10,'normal'))
        self.spinbox_people_4.grid(row=3,column=2,padx=6, sticky=W)

        super().description()
        self.btn_4 = Button(self.pop, text = "Confirm", font= ("Elephant", 8, 'italic'), width = 17, command=self.add_queue_4)
        self.btn_4.grid(row=4, column = 2, padx=5, pady=5)

    def make_press(self, event):
        self.add_queue_4()

    def get_data_4(self):
        self.full_name = self.entry_1.get().strip() +' '+ self.entry_2.get().strip()
        tup = (self.full_name, self.spinbox_people_4.get())
        return tup
    
    def add_queue_4(self):
        try:
            data = self.get_data_4()

            if len(self.entry_1.get()) == 0 and len(self.entry_2.get()) == 0:
                raise TypeError("Please check your Name Surname and amount.")
            
            elif len(self.entry_1.get()) == 0:
                raise NameError("Please check your Name.")
            
            elif len(self.entry_2.get()) == 0:
                raise SyntaxError("Please check your Surname.")
            
            else:
                data_file = open("Num_Super_Splash.txt", 'a')
                for i in range(int(self.spinbox_people_4.get())):
                    self.main_page_instance.fouth_machine.enqueue(data)
                    
                    if self.main_page_instance.laa4.cget("text"):
                        data_file.write(self.entry_1.get().strip() +' '+ self.entry_2.get().strip()+"\n")
                    self.main_page_instance.set_laa4_text(self.main_page_instance.fouth_machine.get_size_element())

                data_file.close()
                tkinter.messagebox.showinfo("", "Yours reservation is successfully")
        
        except ValueError:
            tkinter.messagebox.showerror("", "Please check your entered amount of people.")

        except NameError as error:
            tkinter.messagebox.showerror("", f"{error}")

        except SyntaxError as error:
            tkinter.messagebox.showerror("", f"{error}")
        
        except TypeError as error:
            tkinter.messagebox.showerror("", f"{error}")
            
        self.pop.destroy()


# The CircularQueue class is a data structure that implements a circular queue.
class CircularQueue():
    
    def __init__(self, size):  # initializing the class
        self.size = size
        # initializing queue with none
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        # condition if queue is full
        if ((self.rear + 1) % self.size == self.front):
            pass

        # condition for empty queue
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

        else:
            # next position of rear
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if (self.front == -1):  # condition for empty queue
            pass

        # condition for only one element
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def get_size_element(self):
        if self.front == -1:
            return 0
        elif self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return self.size - (self.front - self.rear - 1) 
                    


first_page_login()

