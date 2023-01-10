from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:

    def __init__(self):
        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # Set up GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)

        self.to_history_button = Button(self.button_frame,
                                        text="History / Export",
                                        bg="#004C99",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        state=DISABLED,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)

        # **** Remove when integrating!! ***
        self.to_history_button.config(state=NORMAL)

    def to_history(self):
        HistoryExport(self)


class HistoryExport:

    def __init__(self, partner):
        # setup dialogue box and background colour
        self.history_box = Toplevel()

        # disable help button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, closes help and
        # 'releases' help button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history,
                                          partner))

        self.history_frame = Frame(self.history_box, width=300,
                                   height=200
                                   )
        self.history_frame.grid()

        self.dismiss_button = Button(self.history_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#666666",
                                     fg="#FFFFFF",
                                     command=partial(self.close_history,
                                                     partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes help dialogue (used by button and x at top of dialogue)
    def close_history(self, partner):
        # Put help button back to normal...
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
