from tkinter import Toplevel, Tk

from Dependencies.Value import Value
from Dependencies.Event import Event

from UIComponents.Window.Window import MakeWindow


root: Tk = Tk()

event = Event()

def HandleEvent(text):
	print(text)

event.Connect(HandleEvent)

event.Fire("test")


value = Value()

value.WillChange.Connect(HandleEvent)
value.Changed.Connect(HandleEvent)

value.Set("BIG TEST")

root.mainloop()