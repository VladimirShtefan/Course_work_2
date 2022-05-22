# Курс 2. Курсовая

Позади самые важные 9 недель обучения, теперь вас ждет подготовка к собеседованию. Необходимо выполнить курсовую работу, чтобы проверить и показать свои знания. Курсовой проект — это точно такое же домашнее задание, его точно так же проверит наставник, просто это задание финальное.

<aside>
💡 ВАЖНО! Сначала **изучить материалы всех пройденных уроков**, а только потом приступать к выполнению курсовой работы.

</aside>

Мы снова пишем игру, на этот раз — в слова. Сыграйте в [игру на сайте Яндекса](https://yandex.ru/games/play/99195), чтобы понять общий принцип. Важная разница: игра будет многопользовательской, а для тестирования вы можете привлечь друга или родственника. 

## Пример работающего приложения

```python

**Программа:** Ввведите имя игрока
**Пользователь:** Василий 

**Программа:** Привет, Василий!
**Программа:** Составьте 8 слов из слова ПИТОН
**Программа**: Слова должны быть не короче 3 букв
**Программа**: Чтобы закончить игру, угадайте все слова или напишите "stop"
**Программа**: Поехали, ваше первое слово?

**Пользователь: пони
Программа: верно

Пользователь: патефон
Программа: неверно

Пользователь: ион
Программа: верно

Пользователь: опт
Программа: верно

Пользователь: пот
Программа: верно

Пользователь: тип
Программа: верно

Пользователь: топ
Программа: верно

Пользователь: пион
Программа: верно

Пользователь: понт
Программа: верно

Программа: слова закончились, игра завершена!
Программа: вы угадали 8 слов**

(программа завершена)
```

```python
**Программа:** Игра начинается
**Программа:** Исходное слово: УПРАЖНЕНИЕ
Программа: можно составить 13 слов
**Программа**: Слова должны быть не короче 3 букв

**Пользователь: руна
Программа: верно

Пользователь: стоп
Программа: игра завершена!
Программа: вы угадали 1 слов**

(программа завершена)
```

Инструкция дальше разбита на шаги, выполните их последовательно.

### Шаг 0

Запишите данные в формате:

```python
[{
    "word": "питон",
     "subwords":  [
         "пони", "ион", "опт", "пот", "тип", "топ", "пион", "понт"
     ]},
    {
      "word": "набор",
      "subwords":  [
          "бар", "бон", "бор", "раб", "бра", "боа", "нора", "роба", "барон"
     ]},
    {
			"word": "строка",
			"subwords": [
         "акр", "акт", "кот", "рак", "орк", "оса", "сок", "ток", "тор", "кора", 
         "коса", "сота", "торс", "роса", "скат", "скат"
     ]
}]
```

```python
Больше слов можно взять здесь:

https://wordhelp.ru/comb/%D0%BD%D0%B0%D0%B1%D0%BE%D1%80 
```

Разместите список слов на внешнем ресурсе, например, [https://jsonkeeper.com/](https://jsonkeeper.com/). Чтобы разместить список, откройте ссылку в браузере,  скопируйте JSON в текстовое поле, нажмите save, скопируйте ссылку в верху экрана. Это и будет путь, по которому хранится JSON. 

![2022-05-05 13.25.19.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d0116aa6-008d-411e-93bb-2ae04286f71b/2022-05-05_13.25.19.gif)

### Шаг 1

Создайте класс `BasicWord` в отдельном файле. Этот класс будет содержать в себе:

**Поля:**

- исходное слово,
- набор допустимых подслов.

**Методы:**

- проверку введенного слова в списке допустимых подслов (вернет bool),
- подсчет количества подслов (вернет int).

**При инициализации** экземпляру задаются: **исходное слово** и набор **допустимых слов,** составленных из исходного. ****

### Шаг 2

Создайте класс `Player`. Этот класс будет содержать в себе:

**Поля:**

- имя пользователя,
- использованные слова пользователя.

**Методы:**

- получение количества слов (возвращает int);
- добавление слова в использованные слова (ничего не возвращает);
- проверка использования данного слова до этого (возвращает bool).

### Шаг 3

Напишите функцию `load_random_word()` в файле `utils`, которая:

- получит список слов с внешнего ресурса,
- выберет случайное слово,
- создаст экземпляр класса `BasicWord`,
- вернет этот экземпляр.

<aside>
💡 Подготовительные шаги завершены, теперь мы пишем основной код программы.

</aside>

### Шаг 4

Напишите стартовую логику: приветствие и вывод слова:

- Импортируйте нужные классы и функции.
- Получите у пользователя его имя.
- Создайте экземпляр класса Player с нужным именем.
- Поздоровайтесь с пользователем.
- Выведите полученное из `load_random_word` случайное слово.
- Предложите сделать первый ход.

```python
**Программа:** Ввведите имя игрока
**Пользователь:** Василий 

**Программа:** Привет, Василий!
**Программа:** Составьте 8 слов из слова ПИТОН
**Программа**: Слова должны быть не короче 3 букв
**Программа**: Поехали, ваше первое слово?
```

### Шаг 5

Запустите цикл (столько раз, сколько подслов в слове).

В каждой итерации получите от пользователя слово, проверьте его с помощью метода экземпляра класса BasicWord. 

Сообщите пользователю, есть ли такое слово.

Если есть, добавляйте слово в список использованных слов класса Player.

Добавьте проверку на `stop`: если пользователь ввел `stop` или `стоп`, то игра прекращается.

### Шаг 6

Выведите количество угаданных слов. Информацию получите из экземпляра класса Player. 

```python
**Программа: слова закончились, игра завершена!
Программа: вы угадали 8 слов!**
```

### Шаг 7

Когда всё готово, протестируйте программу, проверьте свой стиль кода, соответствие требованиям, исправьте ошибки, которые показывает PyCharm, запакуйте файл (или файлы) в ZIP-архив и сдайте на платформу.

### Подсказки

Структура вашего проекта может выглядеть так:

```python
main.py          – это основной файл приложения

players.py       - тут класс игрока
basic_word.py    - тут класс слова

utils.py         - тут лежат функции

```

### Критерии проверки работы

- [ ]  Используются объекты.
- [ ]  Получение данных реализовано в виде функции.
- [ ]  Функции и классы вынесены в отдельные файлы.
- [ ]  Данные загружаются с помощью request.