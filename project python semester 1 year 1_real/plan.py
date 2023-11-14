# import tkinter as tk


# class TimerPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         self.time_left = 60  # Initial time
#         self.timer_label = tk.Label(self, text="")
#         self.timer_label.pack()

#         self.update_timer()  # Start the timer

#         button = tk.Button(self, text="Next Page", command=self.next_page)
#         button.pack()

#     def update_timer(self):
#         if self.time_left > 0:
#             self.timer_label.config(text="Time left: {} seconds".format(self.time_left))
#             self.time_left -= 1
#             self.after(1000, self.update_timer)  # Update every second
#         else:
#             self.timer_label.config(text="Time's up!")

#     def next_page(self):
#         self.controller.show_frame(NextPage)
#         self.controller.frames[NextPage].start_timer()  # Start the timer on the next page


# class NextPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="Next Page")
#         label.pack()

#         button = tk.Button(self, text="Previous Page", command=self.previous_page)
#         button.pack()

#     def previous_page(self):
#         self.controller.show_frame(TimerPage)

#     def start_timer(self):
#         self.after(1000, self.update_timer)  # Start the timer

#     def update_timer(self):
#         print("Update timer")  # Replace this with your own timer update logic
#         self.after(1000, self.update_timer)  # Update every second


# class SampleApp(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.geometry("400x300")
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

#         self.frames = {}
#         for F in (TimerPage, NextPage):
#             frame = F(container, self)
#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")

#         self.show_frame(TimerPage)

#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()


# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()
# import tkinter as tk

# def motion(event):
#     x, y = event.x, event.y
#     print(f'Mouse position: x={x}, y={y}')

# root = tk.Tk()

# # Bind the motion event to the motion function
# root.bind('<Motion>', motion)

# root.mainloop()
print("     b ew l    ".strip())