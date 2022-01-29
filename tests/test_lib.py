from dany.lib import try_me

def test_try_me():
    assert try_me('My number is (703) 666-5025.') == 'Phone number found: (703) 666-5025'
