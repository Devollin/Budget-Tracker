from typing import TypeVar, Generic
from Dependencies.Event import Event


T = TypeVar('T')


class Value(Generic[T]):
	Changed: Event[T] = Event()
	WillChange: Event[T] = Event()

	def __init__(self):
		self.__value: T = None
		
	def Set(self, value: T) -> None:
		self.WillChange.Fire(self.__value)

		self.__value = value

		self.Changed.Fire(self.__value)

	def Get(self) -> T:
		return self.__value

	def Destroy(self):
		self.WillChange = None
		self.Changed = None
		self.__value = None