from main import BooksCollector
# noinspection PyUnresolvedReferences
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_book_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость')

        assert collector.get_book_genre('Гордость') == ''

    @pytest.mark.parametrize('name, genre',
                             [['Черновик', 'Фантастика'], ['Гордость', 'Детективы'], ['Недотепа', 'Мультфильмы'],
                              ['Кошмар', 'Ужасы'], ['Смешно', 'Комедии']])
    def test_set_book_genre_name_corresponds_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_get_the_fiction_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Черновик')
        collector.add_new_book('Гордость')
        collector.add_new_book('Недотепа')
        collector.set_book_genre('Черновик', 'Фантастика')
        collector.set_book_genre('Гордость', 'Детективы')
        collector.set_book_genre('Недотепа', 'Фантастика')

        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    @pytest.mark.parametrize('name, genre', [['Черновик', 'Фантастика'], ['Гордость', 'Детективы'], ['Недотепа', 'Мультфильмы'], ['Кошмар', 'Ужасы'], ['Смешно', 'Комедии']])
    def test_get_books_with_specific_genre_name_corresponds_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_with_specific_genre(genre)[0] == name

    @pytest.mark.parametrize('name, genre', [['Черновик', 'Фантастика'], ['Недотепа', 'Мультфильмы'], ['Смешно', 'Комедии']])
    def test_get_books_for_children_only_children_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert len(collector.get_books_for_children()) > 0

    @pytest.mark.parametrize('name, genre', [['Гордость', 'Детективы'], ['Кошмар', 'Ужасы']])
    def test_get_books_for_children_not_children_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_favorites_name_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость')
        collector.add_book_in_favorites('Гордость')

        assert collector.get_list_of_favorites_books()[0] == 'Гордость'

    def test_add_book_in_favorites_only_favorites_book_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость')
        collector.add_new_book('Кошмар')
        collector.add_book_in_favorites('Гордость')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость')
        collector.add_new_book('Кошмар')
        collector.add_book_in_favorites('Гордость')
        collector.add_book_in_favorites('Кошмар')
        collector.delete_book_from_favorites('Гордость')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_books_genre_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name, genre',
                             [['Черновик', 'Фантастика'], ['Гордость', 'Детективы'], ['Недотепа', 'Мультфильмы'],
                              ['Кошмар', 'Ужасы'], ['Смешно', 'Комедии']])
    def test_get_book_genre_name_corresponds_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    def test_get_list_of_favorites_books_favorites_name_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость')
        collector.add_book_in_favorites('Гордость')

        assert len(collector.get_list_of_favorites_books()) == 1
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector