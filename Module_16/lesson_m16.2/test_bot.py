import bot
import pytest
from unittest.mock import Mock

# Write your message here message.chat.id
# Run bot with command /start and find chat id in console

test_id = 434929317  # user which I tested need to take your chat.id (/start in console in the console will be this id)

msg = Mock()
msg.chat.id = test_id
msg.text = 'Some text'


def test_help():
    answer = bot.help(msg)
    assert "HELP_WORKS" == answer


def test_start():
    answer = bot.handle_start(msg)
    assert "START_WORKS" == answer


def test_text():
    msg.text = 'What films are shown in cinema theaters?'
    answer = bot.text(msg)
    assert 0 == answer

    msg.text = '/films'
    answer = bot.text(msg)
    assert 0 == answer

    msg.text = 'Cinema theater'
    answer = bot.text(msg)
    assert 1 == answer

    msg.text = '/cinema'
    answer = bot.text(msg)
    assert 1 == answer

    msg.text = 'back'
    answer = bot.text(msg)
    assert 2 == answer

    msg.text = 'producers'
    answer = bot.text(msg)
    assert 3 == answer

    msg.text = 'random text'
    answer = bot.text(msg)
    assert 4 == answer


def test_handle_films():
    bot.handle_films(msg)


def test_OMl():
    msg.text = '-'
    answer = bot.OMl(msg)
    assert 0 == answer

    msg.text = '/1'
    answer = bot.OMl(msg)
    assert 0 == answer

    msg.text = '/666'
    answer = bot.OMl(msg)
    assert 1 == answer


def test_first_step():
    bot.first_step(msg)

    answer = bot.first_step(msg)
    assert answer == 'MADE'


def test_second_step():
    msg.text = 'back'
    answer = bot.second_step(msg)
    assert answer == 0

    msg.text = 'SPAM message'
    answer = bot.second_step(msg)
    assert answer == 1

    msg.text = '/'
    answer = bot.second_step(msg)
    assert answer == 2
