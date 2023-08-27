class Field:

    def __init__(self):
        self.value = None

    def set_value(self, x: str):
        self.value = x

    def get_value(self) -> str:
        return self.value


if __name__ == '__main__':
    message = Field()
    message.set_value("Hello")
    print(message.get_value())