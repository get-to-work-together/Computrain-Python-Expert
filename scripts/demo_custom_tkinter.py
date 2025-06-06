import customtkinter as ctk


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.geometry('300x200')  # width x height + x_offset + y_offset
        self.title('tkinter demo')

        self.grid_columnconfigure(0, weight=1)

        self.text1 = ctk.CTkEntry(self)
        self.text1.grid(row=0, column=0, padx=10, pady=6, sticky="ew")

        self.text2 = ctk.CTkEntry(self)
        self.text2.grid(row=1, column=0, padx=10, pady=6, sticky="ew")

        self.button1 = ctk.CTkButton(self, text="Add", command=self.handle_add)
        self.button1.grid(row=3, column=0, padx=10, pady=6)

        self.result = ctk.CTkEntry(self)
        self.result.grid(row=4, column=0, padx=10, pady=6, sticky="ew")

        self.message = ctk.CTkLabel(self, text='')
        self.message.grid(row=5, column=0, padx=10, pady=6, sticky="ew")

    def handle_add(self):
        try:
            self.message['text'] = ''
            number1 = int(self.text1.get())
            number2 = int(self.text2.get())
            value = str(number1 + number2)
            self.result.delete(0, "end")
            self.result.insert(0, value)

        except:
            self.message['text'] = 'An error occured. Not a valid number.'


if __name__ == '__main__':
    app = App()
    app.mainloop()
