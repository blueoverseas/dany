import re

def try_me(text=None):
    """
    Enter a text with an american phone # such as (555) 666-7777
    """
    if text is None:
        print('Input a text with a correctly formatted US phone number:')
        text = input()

    phoneNumRegex = re.compile(r'(\d{3}|\(\d{3}\))?[- .]?\d{3}[- .]\d{4}')
    mo = phoneNumRegex.search(text)
    try:
        return 'Phone number found: ' + mo.group()
    except:
        return 'No phone number found in the text.'

if __name__ == "__main__":
    print(try_me('My number is (415) 555-4242.'))
