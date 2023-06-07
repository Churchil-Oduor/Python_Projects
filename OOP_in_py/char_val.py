class Char:
    def __init__(self, char: str):
        assert len(char) == 1, f"please enter a char type"

        self.__caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__small_caps = __caps.lower()

