import tkinter as tk

def GetLogin(loginWindow: tk.Tk):
	loginWindow.destroy()

def LoginWindow() -> tk.Tk:
	loginWindow = tk.Tk()
	loginWindow.geometry('400x150')
	loginWindow.title("User Login - MyApp")

	#username label and text entry box
	usernameLabel = tk.Label(loginWindow, text="User Name").grid(row=0, column=0)
	username = tk.StringVar(loginWindow)
	usernameEntry = tk.Entry(loginWindow, textvariable=username).grid(row=0, column=1)

	#password label and password entry box
	passwordLabel = tk.Label(loginWindow, text="Password").grid(row=1, column=0)
	password = tk.StringVar(loginWindow)
	passwordEntry = tk.Entry(loginWindow, textvariable=password, show='*').grid(row=1, column=1)

	loggedUser = ""
	loginButton = tk.Button(loginWindow, text="Login", command=lambda: GetLogin(loginWindow)).grid(row=4, column=0)
	loginWindow.mainloop()

	if username.get()!="123":
		return ""
	else:
		return "123"