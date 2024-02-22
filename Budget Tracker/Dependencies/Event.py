from typing import TypeVar, Generic, Callable


T = TypeVar('T')


class Listener(Generic[T]):
	type = "Listener"

	def __init__(self, function: Callable[[T], None]) -> None:
		self.function: Callable[[T], None] = function


class Event(Generic[T]):
	type = "Event"

	def __init__(self) -> None:
		self.__listeners: list[Listener[T]] = []

	def Fire(self, data: T):
		for item in self.__listeners:
			item.function(data)

	def Connect(self, function: Callable[[T], None]) -> None:
		listener = Listener[T](function)

		self.__listeners.append(listener)

	def Destroy(self) -> None:
		self.__listeners.clear()