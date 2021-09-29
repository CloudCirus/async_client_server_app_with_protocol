PROTOCOL = "РКСОК/1.0"
ENCODING = "UTF-8"


class Convertor:

    ENCODING = "UTF-8"

    @staticmethod
    def str_to_bytes(str_or_bytes: str) -> bytes:
        try:
            value = str_or_bytes.encode(ENCODING)
        except Exception as ex:
            print('str_to_bytes exeption', ex)
        return value

    @staticmethod
    def bytes_to_str(str_or_bytes: bytes) -> str:
        try:
            value = str_or_bytes.decode(ENCODING)
        except Exception as ex:
            print('bytes_to_str exeption', ex)
        return value
