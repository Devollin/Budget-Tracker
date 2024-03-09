from tkinter import Toplevel, ttk, dialog


def MakeWindow(title: str | None) -> Toplevel:
	window = Toplevel()
	window.title(title)

	return window