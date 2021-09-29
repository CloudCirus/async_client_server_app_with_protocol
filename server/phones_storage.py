from typing import Union
import os


def _path(name: str) -> str:
    return f'phones_storage/{name}.txt'


class PhonesStorage:
    """Handle data"""

    def __init__(self, name: str, phones: Union[list, None]) -> None:
        self.name = name
        self.phones = phones

    def get_phones(self) -> str:
        if self.is_file_exists():
            with open(_path(self.name), 'r') as f:
                l = [element.strip() for element in f.readlines()]
                phones = '\r\n'.join(l)
                print(f'get phones: {phones} from {_path(self.name)}')
                return phones
        return None

    def write_file(self) -> None:
        with open(_path(self.name), 'w') as f:
            f.writelines(self.phones)
            print(f'write to file: {_path(self.name)}')

    def delete_file(self) -> None:
        os.remove(_path(self.name))
        print(f'file removed: {_path(self.name)}')

    def is_file_exists(self) -> bool:
        return os.path.exists(_path(self.name))
