import re

def try_me(text):
    ### enter a text with an american phone # such as (555) 666-7777 ###
    phoneNumRegex = re.compile(r'(\d{3}|\(\d{3}\))?[- .]?\d{3}[- .]\d{4}')
    mo = phoneNumRegex.search(text)
    return 'Phone number found: ' + mo.group()

if __name__ == "__main__":
    print(try_me('My number is (415) 555-4242.'))
