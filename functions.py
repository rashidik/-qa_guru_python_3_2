def readable(namedz, *args):
    namedz = namedz.__name__.title().replace("_", " ")
    print(namedz, *args)


def open_browser(browser_name):
    readable(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    readable(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    readable(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="name.org")
find_registration_button_on_login_page(page_url="name.org", button_text="login")