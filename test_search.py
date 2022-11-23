from selene.support.shared import browser
from selene import be, have

#Доработайте тест с первого занятия с Pytest

#Выставите размер браузера с помощью фикстуры Pytest

#Добавьте еще один "негативный" тест на поиск, чтобы результат поиска не выдавал результатов

#Запушьте код в свой репозиторий и дайте на него ссылку в качестве ответа на домашнее задание

def test_positive_search(open_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_search(open_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('abrakadabra').press_enter()
    browser.element('[id="trollolo"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))