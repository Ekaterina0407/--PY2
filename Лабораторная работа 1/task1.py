import doctest

class Book:  #  по PEP8 название класса пишется с заглавной буквы
    def __init__(self, author: str, pages: int, last_read_page: int):

        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть типа str")
        self.author = author  # автор

        if not isinstance(pages, (int)):
            raise TypeError("Количество страниц должно быть типа int")
        self.pages = pages  # количество страниц

        self.last_read_pages =  last_read_page
        if not isinstance(last_read_page, (int)):
            raise TypeError("Последняя страница должна быть типа int")

    def is_author_title(self) -> bool:
        """
        Это функция будет проверять: первая буква в верхнем регистре,
        все остальные в нижнем
        :return: Имя автора коректно/не корректно
        """
    def increment_last_read_page(self, read_pages: int):
        """
        Метод увеличивает последнюю прочитанную страницу.

        :param read_pages: Количество прочитанных страниц
        """
        self.last_read_page += read_pages

class VK:
    def __init__(self, people: str, sms: int):
        if not isinstance(people, str):
            raise TypeError("Имя людей должно быть типа str")
        self.people = people  # люди

        if not isinstance(sms, (int)):
            raise TypeError("Количество смс должно быть типа int")
        self.sms = sms  # количество смс

    def is_people_title(self) -> bool:
        """
        Это функция будет проверять: первая буква в верхнем регистре,
        все остальные в нижнем
        :return: Имя людей отображено коректно/не корректно
                """
    def is_sms_positiv(self) -> bool:
        """
        Это функция будет проверять: количество смс должно быть либо > 0, лиибо = 0
        :return: Количество смс отображено корректно/не корректно
                """

class Door:
    def __init__(self, model: str, high: (int, float), max_high: (int, float)):
        if not isinstance(model, str):
            raise TypeError("Название модели должно быть типа str")
        self.model = model  # модель

        if not isinstance(high, (int, float)):
            raise TypeError("высота двери должна быть типа int или float")
        self.high = high  # высота

        if not isinstance(max_high, (int, float)):
            raise TypeError("максимальная высота двери должна быть типа int или float")
        self.max_high = max_high  # высота


    def is_model_language(self) -> bool:
        """
        Это функция будет проверять: модель написана на английском языке
        :return: Модель написана коректно/не корректно
                """
    def is_max_high(self) -> bool:
        """
        Это функция будет проверять: является ли высота двери допустимой
        :return: Высота является допустимой/ не допутсимой
                """

if __name__ == "__main__":
    book = Book('Пушкин А.С.', 1000, 989)
    vk = VK('Ирина Тимофеевна', 50)
    door = Door('Porta', 3.5, 5)
    doctest.testmod()
