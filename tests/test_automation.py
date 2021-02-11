from automation import __version__


def test_version():
    assert __version__ == '0.1.0'

from automation.automation import phone_number, emails

def test_phone_number():
    actual = phone_number()
    expected = open('phone_numbers.txt')
    assert actual == expected

def test_emails():
    actual = emails()
    expected = open('emails.txt')
    assert actual == expected
