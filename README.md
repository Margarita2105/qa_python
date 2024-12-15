# qa_python
test_add_new_book_add_two_books - Проверяет добавление двух книг в словарь books_rating. Используемые методы - add_new_book и get_books_rating

test_add_new_book_book_has_no_genre - Проверяет, что у добавленных книг нет жанра. Используемые методы - add_new_book и get_book_genre

test_set_book_genre_name_corresponds_genre - Проверяет, что книге добавлен жанр и он соответствует добавленному жанру. Используемые методы - add_new_book, set_book_genre и get_book_genre

test_get_books_with_specific_genre_get_the_fiction_genre - Проверяет, что отбираются книги с жанром Фантастика. Используемые методы - add_new_book, set_book_genre и get_books_with_specific_genre


test_get_books_with_specific_genre_name_corresponds_genre - Проверяет, что выводится название книги с заданным жанром. Используемые методы - add_new_book, set_book_genre и get_books_with_specific_genre

test_get_books_for_children_only_children_genre - Проверяет, что возвращаются книги с разрешенным жанром для детей. Используемые методы - add_new_book, set_book_genre и get_books_for_children

test_get_books_for_children_not_children_genre - Проверяет, что не возвращаются книги с запрещенным жанром для детей. Используемые методы - add_new_book, set_book_genre и get_books_for_children

test_add_book_in_favorites_favorites_name_in_list - Проверяет, что возвращается название книги, добавленное в избранное. Используемые методы - add_new_book, add_book_in_favorites и get_list_of_favorites_books

test_add_book_in_favorites_only_favorites_book_in_list - Проверяет, что в избранном только книги, добавленные в избранное. Используемые методы - add_new_book, add_book_in_favorites и get_list_of_favorites_books


test_delete_book_from_favorites_delete_one_book - Проверяет, что при удалении книги из избранного, книга из избранного удаляется. Используемые методы - add_new_book, add_book_in_favorites, delete_book_from_favorites и get_list_of_favorites_books
