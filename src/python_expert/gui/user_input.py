import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("New User")
        # self.geometry("400x150")
        self.grid_columnconfigure((0, 1), weight=1)

        customtkinter.CTkLabel(self, text='Name:').grid(row=0, column=0, padx=10, pady=6, sticky="w")

        self.name = customtkinter.CTkEntry(self)
        self.name.grid(row=0, column=1, padx=10, pady=6, sticky="ew")

        customtkinter.CTkLabel(self, text='E-mail:').grid(row=1, column=0, padx=10, pady=6, sticky="w")

        self.e_mail = customtkinter.CTkEntry(self)
        self.e_mail.grid(row=1, column=1, padx=10, pady=6, sticky="ew")

        customtkinter.CTkLabel(self, text='Password:').grid(row=2, column=0, padx=10, pady=6, sticky="w")

        self.password = customtkinter.CTkEntry(self)
        self.password.grid(row=2, column=1, padx=10, pady=6, sticky="ew")

        customtkinter.CTkLabel(self, text='Group:').grid(row=3, column=0, padx=10, pady=6, sticky="w")

        self.groep = customtkinter.CTkEntry(self)
        self.groep.grid(row=3, column=1, padx=10, pady=6, sticky="ew")

        self.button = customtkinter.CTkButton(self, text="Add User", command=self.button_callback)
        self.button.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        
    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()