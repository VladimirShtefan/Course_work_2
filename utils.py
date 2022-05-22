from requests import get
from random import choice
from basic_word import BasicWord


def load_random_word():
    """
        - получит список слов с внешнего ресурса
        - выберет случайное слово
        - создаст экземпляр класса `BasicWord`
    Returns:
        вернет экземпляр.
    """
    json_words = get('https://jsonkeeper.com/b/ED34')
    rand_word = choice(json_words.json())
    user_word = BasicWord(rand_word['word'], rand_word['subwords'])
    return user_word


def get_ending_word(number, dict_ending_words=None):
    """
        Формирует окончание слова в зависимости от числа перед словом
    Args:
        number: полученное число
        dict_ending_words: словарь с окончаниями

    Returns:
        окончание в виде строки
    """
    if dict_ending_words:
        for key, value in dict_ending_words.items():
            if number >= 0:
                if number % 10 in value:
                    return key
                elif number % 100 in value:
                    return key
        return ''
    return ''
