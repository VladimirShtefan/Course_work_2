from players import Player
from utils import load_random_word, get_ending_word


def main():
    # получаем имя пользователя и создаем экземпляр класса Player
    user_name = input('Введите имя игрока: ')
    user = Player(user_name)
    # получаем рандомное слово, его ответы, а так же длина самого короткого слова в ответах
    word = load_random_word()
    basic_word = word.basic_word.upper()
    len_answer_list = word.get_number_words()
    min_length_word = word.get_min_length_words()
    # прописываем словарь с окончаниями
    end_len_answer_dict = {
        '': [0, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        'о': [1],
        'а': [2, 3, 4]
    }
    end_min_length_word_dict = {
        '': [0, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        'ы': [1]
    }

    print(f'Здравствуй, {user.user_name}!')
    print(f'Составьте {len_answer_list} слов{get_ending_word(len_answer_list, end_len_answer_dict)} из слова {basic_word}')
    print(f'Слова должны быть не короче {min_length_word} букв{get_ending_word(min_length_word, end_min_length_word_dict)}')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print('Поехали, ваше первое слово?')

    stop_program = False
    for i in range(len_answer_list):
        next_word = False
        # если пользователь введет стоп - выходим их цикла
        if stop_program:
            break

        while not next_word:
            user_answer = input('Ответ: ')
            # обработка сообщения Stop
            if 'stop' in user_answer.lower():
                next_word = True
                stop_program = True
                continue
            else:
                # проверяем ответы на корректность и записываем их если они верные
                if user.check_duplication(user_answer):
                    next_word = True
                    if word.check_user_word(user_answer):
                        print('Верно')
                        user.add_word_in_list(user_answer)
                    else:
                        print('Не верно')
                else:
                    print('Такое слово уже было')
    # выдаем результаты игры
    if stop_program:
        print('игра завершена!')
    else:
        print('слова закончились, игра завершена!')
    print(f'вы угадали {user.get_numbers_correct_words()} слов{get_ending_word(user.get_numbers_correct_words(), end_len_answer_dict)}')
    # чтобы не закрывался терминал для многопользовательской игры
    input()


if __name__ == '__main__':
    main()
