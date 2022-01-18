import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

# Additional information about movies are shown in cinema theatres
info_films_dop = ['Movie duration: ', 'Film release year: ', 'Film release in Russia: ',
                  'Age limit: ']
dop_full, dop_full2, dop_full3, dop_full4, dop_full5, href, info_films, proverka, name_cinema, name_metro, id_cinema, \
kino, description = [], [], [], [], [], [], [], [], [], [], [], [], []
pol, pol1, pol2, pol3, pol4, pol5, count, aj, index = 0, 0, 0, 0, 0, 0, 0, 0, 0
dict_cinema = {}
bot = telebot.TeleBot('1265722412:AAEAAWOB92vDfIqjNCghVov3xH9NdmAzECk')
greet_kb = ''

key = types.ReplyKeyboardMarkup(resize_keyboard=True)
films = types.KeyboardButton('What movies are shown in cinema theatres?')

cinema = types.KeyboardButton('Cinema theatres')
creator = types.KeyboardButton('Producers')

key.row(cinema, films)
key.row(creator)


# Message handler '/help'
@bot.message_handler(commands=['help'])
def help(message):
    file_id = 'CAACAgIAAxkBAAJGNF6U37MtDS20PIxt4PFNf3-CXlQrAAJFAANZu_wl-9SkNOET-OsYBA'
    bot.send_sticker(message.chat.id, file_id)
    bot.send_message(message.chat.id,
                     """
    Hi, you called the command /help. It means that you have a problems.
    Ok, beginning to help:
    1. Movies that are on right now - /films
    2. Cinema theaters
    """)
    return "HELP_WORKS"


# Handler command '/start'
@bot.message_handler(commands=['start'])
def handle_start(message):
    print(message.chat.id)
    # bot.delete_message(message.chat.id, message.message_id)  # in testing give an error (No message_id in fact)

    file_id = 'CAACAgIAAxkBAAJGLl6U3tLh48n-8kPCjc0liVkoteGJAAJHAANZu_wlXJ3WrE3fYSwYBA'
    bot.send_sticker(message.chat.id, file_id)

    bot.send_message(message.chat.id, "Hello I am a bot CINEMA GEEKS team.\n I can show movie screening schedule."
                                      "\nTo begin with, I want to explain to you that the code is strange. I am (Bot)"
                                      "not so cleaver to use me in Tesla car.\nThat's why please, don't bother me with"
                                      "your messages. In command /help everything is written.\nFor start write /films"
                                      "and you will get 100 movies are shown in Saint-Petersburg.\nAlso there is a "
                                      "command /cinema that shows all cinema theatres in Saint-Petersburg. After select"
                                      "it shows schedule.",
                     reply_markup=key, parse_mode='markdown', disable_web_page_preview=True)
    return "START_WORKS"


# @bot.message_handler(commands=['films'])
def handle_films(message):
    global count, aj
    global href_films, proverka, kino
    href_films = []
    data1 = requests.get('https://spb.kinoafisha.info/movies/')

    assert data1.status_code == 200  # For pytest testing

    data = data1.text
    bs = BeautifulSoup(data, 'html.parser')
    elms = bs.select('div.films_right a')

    for x in elms:
        count += 1
        href_films.append(x.attrs['href'])  # Add to array links for parsing description and sessions

    elms2 = bs.select('span.link_border')  # Search all movies names
    for x in elms2:
        if x.text == 'Movies in run':  # limit to 'buttons' panel
            break
        else:
            aj += 1
            if aj <= 100:
                kino.append('"' + x.text + '"' + " - /" + str(aj))

    bot.send_message(message.chat.id, '\n'.join(kino))
    kino = []
    aj = 0
    key = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, 'Choose movie number: ', reply_markup=key)
    bot.register_next_step_handler(msg, OMl)


def OMl(message):
    global change_films, change_films_2
    global description
    global info_films, greet_kb
    change_films = message.text
    change_films_2 = change_films.lstrip('/')

    if change_films.lower == 'exit' or change_films == '-':
        return 0
    else:
        try:
            try:
                data1 = requests.get(href_films[int(change_films_2) - 1])  # parsing description and movie sessions

                assert data1.status_code == 200

                data = data1.text
                bs = BeautifulSoup(data, 'html.parser')
                elms3 = bs.select('span.movieInfoV2_descText p')  # description parsing

                for i in elms3:
                    description.append(i.text)

                elms4 = bs.select('span.movieInfoV2_infoData')  # parsing movie release

                for i in elms4:
                    info_films.append(i.text)

                for o in range(len(info_films)):
                    try:
                        description.append(info_films_dop[o] + info_films[o])

                    except IndexError as e:
                        print(f"IndexError: {e}")
                        return 1

                # bot.delete_message(message.chat.id, message.message_id)
                # In testing give an error (No message_id in fact)
                bot.send_message(message.chat.id, '\n\n'.join(description), reply_markup=key)
                description, info_films = [], []

            except IndexError as e:
                print(f"IndexError: {e}")
                bot.send_message(message.chat.id, "No such movie number. Start over - /films")
                return 1
        except ValueError as e:
            print(f"ValueError: {e}")
            bot.send_message(message.chat.id, "You didn't enter the movie number. Start over - /films")
            return 1

    return 0  # All is Ok


a, b, c, d, e, f = [], [], [], [], [], []
count, index, ind, count2 = 0, 0, 0, 1
time_none = 4
fa, fo = '', ''


def first_step(message):
    global count, fa, fo, count2, b, a, c
    a = []
    fa, fo, count2 = '', '', 1
    c = []
    data1 = requests.get('https://spb.kinoafisha.info/cinema/')

    assert data1.status_code == 200

    data = data1.text
    bs = BeautifulSoup(data, 'html.parser')
    elms = bs.select('a.theater_name.link.link-default')

    for i in elms:
        count += 1
        if count < 183:
            b.append(i.attrs['href'])  # Cinema theaters links
    elms = bs.select('div.theater_right')
    count = 0

    for i in elms:
        count += 1
        if count < 183:
            a.append(i.text.rstrip('\n').lstrip('\n'))  # Cinema theaters list

    for i in a:
        if len(fa) < 4000:
            fa += i + ' - /' + str(count2) + '\n\n'
            count2 += 1
        else:
            fo += i + ' - /' + str(count2) + '\n\n'
            count2 += 1

    bot.send_message(message.chat.id, fa)

    key = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('back')
    key.row(back)
    msg = bot.send_message(message.chat.id,
                           fo + "\nSelect cinema to view the schedule. Or press 'back' button.",
                           reply_markup=key)
    bot.register_next_step_handler(msg, second_step)
    return 'MADE'


def second_step(message):
    global ind, b, c, d, f, data1
    change_of_cinema = message.text
    wordUp = set('!@#$%^&*(){}[]<>,.:;"№%-_+=qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
                 'йцукенгшщзхъёфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪЁФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')

    if change_of_cinema == 'Back' or change_of_cinema == 'back' \
            or change_of_cinema == 'Exit' or change_of_cinema == 'exit':
        # bot.delete_message(message.chat.id, message.message_id)
        # In testing give an error (No message_id in a fact)
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        films = types.KeyboardButton("What movies are shown in cinema theaters?")

        cinema = types.KeyboardButton('Cinema theaters')
        creator = types.KeyboardButton('Producers')

        key.row(cinema, films)

        key.row(creator)
        bot.send_message(message.chat.id, 'You came back.', reply_markup=key)
        ind, b, c, d, f = 0, [], [], [], []
        return 0
    elif any(x for x in wordUp if x in change_of_cinema):
        bot.send_message(message.chat.id, "You entered wrong thing.")
        return 1
    else:
        if change_of_cinema.lstrip('/') == ' ' or change_of_cinema.lstrip('/') == '':
            bot.send_message(message.chat.id, "You entered only '/'")
            return 2
        else:
            change_of_cinema_2 = change_of_cinema.lstrip('/')
            try:
                try:
                    data1 = requests.get(b[int(change_of_cinema_2) - 1])
                except ValueError:
                    pass
            except IndexError:
                pass
            data = data1.text
            bs = BeautifulSoup(data, 'html.parser')
            elms = bs.select('div.showtimes_item.fav.fav-film')
            # Here
            for i in elms:
                c.append(i.text.split('\n'))
            for i in c:
                for j in i:
                    if j == '' or j == 'Buy':
                        pass
                    else:
                        d.append(''.join(j))  # Schedule and price
            list_janre = ['anime', 'biographic', 'action', 'western', 'military', 'detective', 'children`s',
                          'documentary', 'drama', 'historic', 'filmmix', 'comedy', 'concert', 'short', 'crime',
                          'melodrama', 'mystic', 'music', 'cartoon', 'musical', 'scientific', 'adventure',
                          'reality-show', 'family', 'sport', 'tok-show', 'thriller', 'horror', 'fantastic',
                          'fantasy', 'erotic']

            for i in enumerate(d):
                for j in range(len(list_janre)):
                    if list_janre[j] in i[1]:
                        del d[i[0]]
                        break
            for i in enumerate(d):
                if '₽' in i[1]:
                    del d[i[0]]
            elms = bs.select('a.theaterInfo_addr.link.link-default')  # Address
            address_of_cinema = []
            for i in elms:
                address_of_cinema.append(i.text.rstrip('\n'))
            elms = bs.select('div.theaterInfo_desc')  # Cinema description
            desc_of_cinema = []
            for i in elms:
                desc_of_cinema.append(i.text)
            bot.send_message(message.chat.id, 'Address: ' + address_of_cinema[0])
            bot.send_message(message.chat.id, 'Description: ' + '\n'.join(desc_of_cinema))
            bot.send_message(message.chat.id, 'Schedule: ' + '\n'.join(d))
            address_of_cinema, desc_of_cinema, d, data, change_of_cinema_2, change_of_cinema = [], [], [], "", 0, 0
            return 3


# Handler command '/text'
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'What movies are shown in cinema theaters?' or message.text == '/films':
        handle_films(message)
        return 0
    elif message.text == 'Cinema' or message.text == '/cinema':
        first_step(message)
        return 1
    elif message.text == 'Back':
        bot.send_message(message.chat.id, 'You came back.', reply_markup=key)
        return 2
    elif message.text == 'Producers':
        bot.send_message(message.chat.id,
                         "This telegram bot was create by team <b>CINEMA</b> <b>GEEKS</b> \n\n<b>Head of</b> "
                         "<b>project:</b> <i>Shihanov</i> <i>Denis</i> \n<b>Tester:</b> <i>Kochetkova</i> "
                         "<i>Kristina</i> \n<b>Developer:</b> <i>Petrashova</i> <i>Polina</i> \n<b>Analytic:</b> "
                         "<i>Brodskiy</i> <i>Daniil</i>",
                         parse_mode='html')
        return 3
    else:
        file_id = 'CAACAgIAAxkBAAJGQF6U4kMttgJ89FlDzfgvRnlNQeLYAAI-AANZu_wlyJTG0rxrt0kYBA'
        bot.send_sticker(message.chat.id, file_id)
        bot.send_message(message.chat.id, 'I don`t understand you 😭')
        return 4


if __name__ == '__main__':
    print('start')
    bot.polling(none_stop=True)
