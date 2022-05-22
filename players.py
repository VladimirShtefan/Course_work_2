class Player:
    def __init__(self, user_name=None):
        self.user_name = user_name or 'User'
        self.user_words_list = []

    def add_word_in_list(self, user_word):
        """
            Добавление слова в использованные слова (ничего не возвращает).
        Args:
            user_word:  ответ пользователя

        Returns:

        """
        self.user_words_list.append(user_word.lower())

    def check_duplication(self, user_word):
        """
            Проверка использования данного слова до этого (возвращает bool).
        Args:
            user_word:

        Returns:

        """
        if user_word.lower() in self.user_words_list:
            return False
        return True

    def get_numbers_correct_words(self):
        """
            Получение количества отгаданных слов (возвращает int).
        Returns:

        """
        return len(self.user_words_list)
