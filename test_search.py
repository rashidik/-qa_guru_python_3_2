from selene.support.shared import browser
from selene import be, have

#Доработайте тест с первого занятия с Pytest

#Выставите размер браузера с помощью фикстуры Pytest

#Добавьте еще один "негативный" тест на поиск, чтобы результат поиска не выдавал результатов

#Запушьте код в свой репозиторий и дайте на него ссылку в качестве ответа на домашнее задание

def test_positive_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('макаки').press_enter()
    browser.element('[id="search"]').should(have.text('макаки'))
def test_negative_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('41212sdfasda').press_enter()
    browser.element('[id="topstuff"]').should(have.text('По запросу 41212sdfasda ничего не найдено. '))