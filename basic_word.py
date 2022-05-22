class BasicWord:
    def __init__(self, basic_word=None, list_words=None):
        self.basic_word = basic_word
        self.list_words = list_words

    def check_user_word(self, user_word):
        """
            Проверку введенного слова в списке допустимых подслов (вернет bool).
        Args:
            user_word: ответ пользователя.
        Returns:

        """
        if user_word.lower() in self.list_words:
            return True
        return False

    def get_number_words(self):
        """
            Подсчет количества подслов (вернет int).
        Returns:

        """
        return len(self.list_words)

    def get_min_length_words(self):
        """
            Подсчет минимальной длины слова из подслов (вернет int).
        Returns:

        """
        min_length = min(self.list_words, key=len)
        return len(min_length)


