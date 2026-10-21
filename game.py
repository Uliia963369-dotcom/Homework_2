from morse import english_to_morse
import random 

WORDS = ['code', 'bit', 'list', 'soul', 'next', 'little',
         'snake', 'mouse']



def get_random_word(): 
    """ 
    Возвращает случайное слово из списка WORDS. 
    Returns: 
        str: Случайное слово из списка 
    """
    import  random
    return random.choice(WORDS)
 


def print_statistics(answers): 
    """ 
    Выводит статистику ответов пользователя. 
    Args: 
        answers (list): Список булевых значений (True/False) 
    """ 
    total = len(answers) 
    correct = sum(answers)  # Более эффективный способ подсчета True 
    incorrect = total - correct 
     
    print(f"\nВсего вопросов: {total}")
    print(f"Верных ответов: {correct}" )
    print(f"Неверных ответов: {incorrect}") 
    
    

def play_game():
    """
    Проводит игру "Угадай слово!"
    Возвращает рандомное слово 
     Args: str: Английское слово
    Возвращает правильный ответ и оценивает полученный
    Возвращает статистику правильных и неправильных ответов 
    
    """
    print("Игра 'Угадай слово!\nУгадай 5 слов по их коду из азбуки морзе:")

    answers = []

    for number in range(1,6): 
      word = get_random_word()
      morse_word = english_to_morse(word)
      print(f"Слово {number}:{morse_word}") 


      user_answer = input("Введите перевод:").strip().lower()
    

      if user_answer == word:
        print("Верно!Вы угадали!")
        user_answer = True
        answers.append(user_answer)
      else:
       user_answer = False
       print(f"Неверно.Зашифрованно было: {word}")
      answers.append(user_answer)
     
    print_statistics(answers)
    


         
    
    
