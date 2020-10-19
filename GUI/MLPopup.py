import tkinter as tk
from Constants import Time, Constants
from Database.Database import Database
import datetime

class MLPopup(tk.Tk):

    def __init__(self, title, *args, **kwargs):
        # Get current weekday
        self.today = Time.WEEKDAYS[datetime.datetime.today().weekday()+1]
        self.exams = []
        # Get all exams and store them in self.exams
        for day in Time.WEEKDAYS[1:]:

            for i in range(len(Time.HOURS)):
                data = Database.pick(day, i)

                if data != {}:
                    if data['type'] == "Exam":
                        if data not in self.exams:
                            self.exams.append(data)

        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry(Constants.POPSIZE)
        self.resizable(False, False)
        self.title(title)
        self.protocol("WM_DELETE_WINDOW", self.destroyFrame)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self._buildFrame()

    def _buildFrame(self):
        """This method should be overriden in child classes"""
        pass

    def destroyFrame(self):
        """Destroy the window"""
        self.quit()
        self.destroy()