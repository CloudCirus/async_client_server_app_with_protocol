from typing import Union


class Data:
    """working with data"""

    def __init__(self, data: str) -> None:
        self.recv_data = data
        self.parsed_data = self.__parse()
        self.name = None

    def __parse(self) -> None:
        """use data string from self.recv, parse it and collect in self.parsed_data"""
        print('parse data...', self.recv_data, sep='\n')
        # parse list with strings
        _strings = self.recv_data.split('\r\n')[:-2]
        # list with first string elements
        _first_string_elements = _strings[0].split()
        command = _first_string_elements[0]
        try:
            name = ' '.join(_first_string_elements[1:-1])
        except Exception as ex:
            print('>>> server.parse_recived_dara', ex, sep='\n')

        parsed_data = [command, name]

        if len(_strings) > 1:
            phones = list()
            for phone in range(len(_strings)-1):
                phone = _strings[-1]
                phones.append(phone)
            parsed_data.append(phones)

        print('ready...', parsed_data, '\n', sep='\n')
        return parsed_data

    def get_command(self) -> str:
        """use self.parsed_data and rerurn command string"""
        print('command:', self.parsed_data[0])
        return self.parsed_data[0]

    def get_name(self) -> Union[str, None]:
        """use self.parsed_data and rerurn name string or None"""
        if len(self.parsed_data) < 2:
            print('name:', None)
            return None
        else:
            print('name:', self.parsed_data[1])
            self.name = self.parsed_data[1]
            return self.name

    def get_phones(self) -> Union[str, None]:
        """use self.parsed_data and rerurn phones string or None"""
        if len(self.parsed_data) > 2:
            print('phones:', self.parsed_data[2])
            return self.parsed_data[2]
        else:
            print('phones:', None)
            return None
