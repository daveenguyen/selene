import os

from selenium import webdriver

from selene import browser
from selene.support.conditions import be
from selene.support.conditions import have
from selene.support.jquery_style_selectors import s, ss
from tests.acceptance.helpers.helper import get_test_driver


def setup_module(m):
    browser.set_driver(get_test_driver())


def teardown_module(m):
    browser.driver().quit()


def test_filter_tasks():
    browser.open_url('file://' + os.path.abspath(os.path.dirname(__file__)) + '/../../resources/todomvcapp/home.html')

    s('#new-todo').should(be.enabled).set_value('a').press_enter()
    s('#new-todo').should(be.enabled).set_value('b').press_enter()
    s('#new-todo').should(be.enabled).set_value('c').press_enter()

    ss("#todo-list>li").should(have.texts('a', 'b', 'c'))
