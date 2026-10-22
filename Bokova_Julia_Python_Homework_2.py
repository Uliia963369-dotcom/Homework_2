from morse import english_to_morse

from morse import  morse_to_english

from game import play_game




def main():  
 """ 
Основная функция программы, управляющая всеми режимами работы.
 
  """ 
 name = input("Добрый день! Введите ваше имя:\n").strip() 

 while True:
  print(f"Отлично,{name}! Выберите режим работы:\n")
  print(f"1 - шифрование (английский -> Морзе)") 
  print(f"2 - дешифрование (Морзе -> английский)")
  print(f"3 - Игра «Угадай слово» (5 вопросов)")
  print(f"4 - Выход") 
 
  user_answer = input().strip()


  if user_answer == "1":
     print("Значит будем шифровать английский текст в код морзе!")
     print("Введи английское текст:")
     english_word = input()
     print(f"Закадированный текст:{english_to_morse(english_word)}") 
           
  elif user_answer == "2": 
     print("Значит будем расшифровывать текст!")
     print("Введите символы азбуки морзе:")
     morse_word = input()
     print(morse_to_english(morse_word))
 
  elif user_answer == "3": 
     
     play_game()
      
  elif user_answer == "4":
       print("До встречи!")
       exit()
  else:       
    print("Ошибка!Вводите только предложенные значения!")
    
     
if __name__ =="__main__":
     main()
 