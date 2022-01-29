from dany.lib import try_me

def test_try_me():
    print('call try_me() with a text containing a phone # with correct format')
    assert try_me('My number is (703) 666-5025.') == 'Phone number found: (703) 666-5025'
    print('call try_me() with a text containing a phone # with incorrect format')
    assert try_me('My number is 7036665025.') == 'No phone number found in the text.'
    print('call try_me() with a text not containing any #')
    assert try_me('M') == 'No phone number found in the text.'
