from selene import browser, be, have


def test_google_request():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_demoqa_text_box():
    browser.open('https://demoqa.com/text-box')
    browser.element('input[id=userName]').should(be.blank).type('Ivan Ivanov')
    browser.element('input[id=userEmail').should(be.blank).type('test@test.com')
    browser.element('button[id=submit]').click()

def test_google_request_trash():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('!9#kk@@9090&fhrgd').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу !9#kk@@9090&fhrgd ничего не найдено. '))