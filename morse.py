WORDS = ['code', 'bit', 'list', 'soul', 'next', 'little', 'snake', 'mouse']


MORSE_DICT = { 
"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", 
"5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", 
"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
"g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", 
"m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", 
"s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", 
"y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..", 
"!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.", 
 
    ")": "-.--.-", " ": "/" 
}
 
 
def english_to_morse(text): 
    """ 
    Переводит английский текст в код Морзе. 
    Args: 
        text (str): Строка на английском языке 
    Returns: 
        str: Текст, преобразованный в код Морзе 
    """ 
    morse_text = [] 
     
    for char in text:
        if char in MORSE_DICT: 
            morse_text.append(MORSE_DICT[char])
        else:
            print("Ошибка!Запустите программу снова!")
            exit() 
            
    return " ".join(morse_text)

     
def morse_to_english(morse_text): 
    """
    Переводит код Морзе обратно в английский текст. 
    Args: 
        morse_text (str): Текст в коде Морзе 
         
    Returns: 
        str: Декодированный английский текст 
    """ 
    reverse_morse_dict = {v: k for k, v in MORSE_DICT.items()} 
     
    english_text = [] 
    
    for code in morse_text.split(): 
        if code in reverse_morse_dict: 
            english_text.append(reverse_morse_dict[code])
        else:
            print("Ошибка!Запустите программу снова!")
            exit()
                 
    return f"Переведенный текст:\n > {"".join(english_text)}"








