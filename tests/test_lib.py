from dany.lib import try_me

def test_try_me_1():
    assert try_me('My number is (703) 666-5025.') == 'Phone number found: (703) 666-5025'


def test_try_me_2():
    assert try_me('My number is 7036665025.') == 'No phone number found in the text.'


def test_try_me_3():
    assert try_me('M') == 'No phone number found in the text.'
