from abc import ABC, abstractmethod

class FileSystemElement(ABC):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

class File(FileSystemElement):
    def __init__(self, file_name: str, file_size: int):
        self._file_name = file_name
        self.__file_size = file_size

    def display(self, level=0) -> None:
        print("  " * level, f"- {self._file_name}: {self.__file_size} bytes")

    def get_size(self) -> int:
        return self.__file_size

class Directory(FileSystemElement):
    def __init__(self, directory_name: str):
        self._directory_name = directory_name
        self.__contents: list[FileSystemElement] = []

    def display(self, level=0) -> None:
        print("  " * level, "-", self._directory_name)
        for fs_element in self.__contents:
            fs_element.display(level + 1)

    def get_size(self) -> int:
        return sum(fs_element.get_size() for fs_element in self.__contents)#sum(fs_element.get_size() for fs_element in self.__contents)

    def add(self, fs_element: FileSystemElement) -> None:
        self.__contents.append(fs_element)
