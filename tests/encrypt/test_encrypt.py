from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    #  Testing valid input: even & uneven key
    assert encrypt_message('Python', 3) == 'tyP_noh'
    assert encrypt_message('Software', 6) == 'er_awtfoS'
    assert encrypt_message('engineering', 5) == 'nigne_gniree'
    assert encrypt_message('sweethome', 2) == 'emohtee_ws'

    #  Testing invalid key type
    with pytest.raises(TypeError):
        encrypt_message('algorithm', 'key_invalid')

    #  Testing invalid messsage type
    with pytest.raises(TypeError):
        encrypt_message(123456, 4)

    #  Testing key outside definied range
    assert encrypt_message('cheers', 8) == 'sreehc'
