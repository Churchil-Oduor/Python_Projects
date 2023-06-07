
class rot13:
    def __init__(self, text: str):
        assert text != ' ', f"You entered an empty string"
        self.__text = text
        self.__alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.__caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__encrypted = ''


    def __encrypt(self):

        for char in self.__text:
            num = self.__alphabet.find(char)
            cnum = self.__caps.find(char)
            if char.isalpha() and num >= 0:
                # check if it is a character
                    
                if num < 13:
                    num += 13
                    new_char = self.__alphabet[num]
                    self.__encrypted += new_char

                else:
                    num -= 13
                    new_char = self.__alphabet[num]
                    self.__encrypted += new_char

            elif char.isalpha() and cnum >= 0:
                if cnum < 13:
                    cnum += 13
                    new_char = self.__caps[cnum]
                    self.__encrypted += new_char

                else:
                    cnum -= 13
                    new_char = self.__caps[cnum]
                    self.__encrypted += new_char

            else:
                self.__encrypted += char

    def  __str__(self):
        self.__encrypt()
        return f"{self.__encrypted}"
    
    
# Happy Hacking