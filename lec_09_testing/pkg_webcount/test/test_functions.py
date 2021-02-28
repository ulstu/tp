from unittest.mock import Mock, patch, PropertyMock
import webcount as w
#from webcount import most_common_word_in_web_page, magic_func

def test_with_patch():
    mock_requests = Mock()
    mock_requests.get.return_value.text = 'aaaa bbb c'
    with patch('webcount.functions.requests', mock_requests):
        result = w.most_common_word_in_web_page(
            ['a', 'b', 'c'],
            'https://python.org/',
        )
    assert result == 'a', \
        'most_common_word_in_web_page tested with test double'
    assert mock_requests.get.call_count == 1
    assert mock_requests.get.call_args[0][0] \
            == 'https://python.org/', 'called with right URL'


def test_magic():
    with patch('webcount.functions.AClass.a', new_callable=PropertyMock) as mock_my_property:
        mock_my_property.return_value = 6
        result = w.functions.magic_func()

    assert result == 6, \
        'most_common_word_in_web_page tested with test double'
