from Dependencies.Value import Value
from Dependencies.Event import Event

event = Event()

def HandleEvent(text):
	print(text)

event.Connect(HandleEvent)

event.Fire("test")


value = Value()

value.WillChange.Connect(HandleEvent)
value.Changed.Connect(HandleEvent)

value.Set("BIG TEST")