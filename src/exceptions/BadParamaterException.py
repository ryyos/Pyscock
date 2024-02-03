class BadParamaterException(Exception):
    def __init__(self) -> None:
        super().__init__('Please enter the value according to the provisions')