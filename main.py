import customtkinter as ctk
from screens import MainMenu  

# App settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class HangmanApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hangman Game")
        self.geometry("900x700")
        self.resizable(False, False)

        self.current_screen = None
        self.show_main_menu()

    def clear_screen(self):
        if self.current_screen:
            self.current_screen.destroy()
            self.current_screen = None

    def show_main_menu(self):
        self.clear_screen()
        self.current_screen = MainMenu(self)
        self.current_screen.pack(fill="both", expand=True)


# Run app
if __name__ == "__main__":
    app = HangmanApp()
    app.mainloop()