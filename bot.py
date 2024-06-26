import telebot
from telebot import types

bot = telebot.TeleBot('6488827969:AAHJAVOftbX77CERku2Eqz6eePlhAxHNV_M')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('👋 Поздороваться')
    markup.add(btn1)
    bot.send_message(message.from_user.id, 'Чтобы начать работу, нажмите   "👋 Поздороваться"', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Поздороваться':
        bot.send_message(message.from_user.id,
                         'Добро пожаловать в Telegram-бота, который расскажет всё о геральдике Югры!')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('❓ Что такое геральдика?')
        btn2 = types.KeyboardButton('🦣 Геральдика ХМАО-Югры')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '👇 Выберите интересующий раздел', reply_markup=markup)

    elif message.text == '❓ Что такое геральдика?':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.from_user.id,
                         'Геральдика (от лат. heraldus — «глашатай») — '
                         'специальная историческая дисциплина, занимающаяся изучением гербов, '
                         'а также традиций и практики их использования.\n'
                         'Является частью эмблематики '
                         '— группы взаимосвязанных дисциплин, изучающих эмблемы. \n'
                         'Отличие гербов от других эмблем заключается в том, что строение, '
                         'употребление и правовой статус гербов соответствуют особым, '
                         'исторически сложившимся правилам. \n'
                         'Геральдика точно определяет, '
                         'что и как может быть нанесено на государственный герб, фамильный герб и так далее, '
                         'объясняет значение тех или иных фигур. \n'
                         'Корни геральдики уходят в Средневековье, '
                         'когда и был разработан специальный геральдический язык. \n'
                         '\n'
                         'Знаток геральдики — геральдист, геральдик, гербовед или арморист. \n'
                         '\n'
                         '10 июня празднуется Международный день геральдики.')
        btn_back = types.KeyboardButton('📚 К разделам')
        markup.add(btn_back)
        bot.send_message(message.from_user.id, 'Чтобы вернуться назад, нажмите "К разделам 📚"',
                         reply_markup=markup)

    elif message.text == '🦣 Геральдика ХМАО-Югры' or message.text == '📜 К темам':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.from_user.id, 'Как и у остальных субъектов РФ, у ХМАО-Югры есть свой герб. '
                                               'В этом разделе Вы можете ознакомиться с 📔 Историей герба '
                                               'и отдельными его 🔍 Элементами.')

        btn_history = types.KeyboardButton('📔 История')
        btn_coat_of_arms = types.KeyboardButton('🔍 Элементы герба')
        markup.add(btn_history, btn_coat_of_arms)
        bot.send_message(message.from_user.id, '👇 Выберите интересующую тему', reply_markup=markup)

    elif message.text == '📔 История':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.from_user.id, 'Если говорить об истории герба ХМАО-Югры, то на 2023 год '
                                               'она насчитывает 28 лет. Можно подумать, что это не так много. '
                                               'Однако даже за такой, казалось бы, короткий промежуток времени '
                                               'регион успел завести себе аж 2 герба!\n'
                                               '\n'
                                               'Югорчане хорошо помнят самый первый герб округа, принятый в 1995 году. '
                                               'Он представлял собой серебряную эмблему, расположенную на подкладе '
                                               'двух '
                                               'щитов, вписанных один в другой, и воспроизводящую стилизованный символ '
                                               '«Кат ухуп вой» в поле рассеченного лазоревого '
                                               'и зелёного щита. Контур щита обведён золотом. '
                                               'Фигурный щит вписан в прямой щит красного цвета, представляющий собой '
                                               'прямоугольник с фигурным заострением в нижней части. Щит увенчан '
                                               'элементом белого цвета, выполненным в орнаментальном стиле обских '
                                               'угров, '
                                               'и окружен венком из зеленых кедровых ветвей. Девиз «Югра» начертан '
                                               'серебряными литерами на лазоревой ленте, расположенной под щитом. '
                                               'Корона, выполненная в форме рогов олицетворяет основное занятие '
                                               'коренного населения — оленеводство. Хвойные ветви являются символом '
                                               'флоры региона. Синий цвет символизирует красоту и величие. '
                                               'Зелёный цвет обозначает жизнь. Белый цвет обозначает снега.')

        bot.send_photo(message.from_user.id, photo='https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/'
                                                   'Coat_of_arms_of_Yugra_%281995%29.svg/800px-Coat_of_arms_of_Yugra'
                                                   '_%281995%29.svg.png')
        btn_back = types.KeyboardButton('👀 Дальше')
        markup.add(btn_back)
        bot.send_message(message.from_user.id, 'Чтобы увидеть продолжение, нажмите "👀 Дальше"',
                         reply_markup=markup)

    elif message.text == '👀 Дальше':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.from_user.id, 'Принятый в 1995 году герб '
                                               'не был внесён как противоречащий правилам геральдики. '
                                               'При экспертизе в 2008 году Геральдический совет при Президенте РФ '
                                               'высказал следующие замечания: \n'
                                               '\n'
                                               'Венки, окружающие гербовые щиты, '
                                               'указывают на то, что владелец герба полностью лишен прав суверенитета '
                                               'и самостоятельности, тогда как округ является суверенным субъектом '
                                               'РФ.\n'
                                               '\n'
                                               'Использованный прием «щит в щите» толкуется таким образом, '
                                               'что при своем формировании автономный округ завоевал некую другую '
                                               'территорию.\n'
                                               '\n'
                                               'Синяя лента с надписью «Югра» символизирует то, что регион '
                                               'был награжден орденом Андрея Первозванного, что также не соответствует '
                                               'действительности.\n'
                                               '\n'
                                               'Кроме того на девизной ленте должен размещаться '
                                               'девиз, а не название региона.')
        btn_back = types.KeyboardButton('👁️ Дальше')
        markup.add(btn_back)
        bot.send_message(message.from_user.id, 'Чтобы увидеть продолжение, нажмите "👁️ Дальше"',
                         reply_markup=markup)

    elif message.text == '👁️ Дальше':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.from_user.id, 'Первая попытка привести герб в '
                                               'соответствие с правилами была предпринята в 2017 году, '
                                               'однако этот вариант был холодно встречен общественностью. Тогда было '
                                               'решено '
                                               'продолжить дискуссию.\n'
                                               '\n'
                                               'В 2019 году на обсуждение общественности было '
                                               'предоставлено четыре варианта обновлённого герба (различающиеся цветом '
                                               'медведей-щитодержателей и формой короны, венчающий щит), созданных с '
                                               'учётом замечаний экспертов и общественности к варианту 2017 года.\n'
                                               '\n'
                                               'В 2020 проект герба был доработан — медведей-щитодержателей сделали '
                                               'золотыми; щит венчает земельная корона, отражающая статус Югры как '
                                               'субъекта РФ, а из её центрального зубца стал вырываться огонь, '
                                               'символизирующий нефтегазовый промысел региона (созвучно изображению '
                                               'земельной короны герба ЯНАО).\n'
                                               '\n'
                                               '24 декабря его утвердил окружной '
                                               'парламент, внеся изменения в закон о флаге и гербе автономного округа. '
                                               '8 февраля 2021 года новый герб был внесён в геральдический регистр '
                                               'России. До 1 января 2022 года был предусмотрен переходный период, '
                                               'в течение которого допускалось использование обоих вариантов герба.')
        btn_back = types.KeyboardButton('💭 Дальше')
        markup.add(btn_back)
        bot.send_message(message.from_user.id, 'Чтобы увидеть продолжение, нажмите "💭 Дальше"',
                         reply_markup=markup)

    elif message.text == '💭 Дальше':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.from_user.id, 'Таким образом, с 2020 года ХМАО-Югра имеет новый герб. '
                                               'Многие встретили его с некоторым недовольством, некоторые высказывали '
                                               'свои замечания по поводу определённых его частей. Говоря о своём '
                                               'личном мнении, я хочу отметить, что новый герб мне понравился: он '
                                               'яркий, торжественный и по праву может являться символом ХМАО-Югры - '
                                               'уникального, самобытного и очень интересного региона со своим '
                                               '"характером" и традициями.')

        btn_back = types.KeyboardButton('📜 К темам')
        markup.add(btn_back)
        bot.send_message(message.from_user.id, 'Чтобы вернуться к темам, нажмите "📜 К темам"',
                         reply_markup=markup)

    elif message.text == '🔍 Элементы герба':
        markup = types.ReplyKeyboardMarkup()
        bot.send_photo(message.from_user.id,
                       photo='https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Yugra_'
                             '(Khanty-Mansia).svg?uselang=ru')
        bot.send_message(message.from_user.id,
                         'Геральдическое описание:\n'
                         '\n'
                         'В рассечённом лазоревом и зелёном поле серебряная птица «Кат ухуп вой» – с двумя, '
                         'подобными орлиным, головами на длинных шеях, '
                         'четырьмя лапами и видимым между головами и шеями хвостом, '
                         'подобным павлиньему и широко просечённым в цвета поля. \n'
                         '\n'
                         'Щит увенчан золотой земельной короной о семи видимых зубцах, '
                         'средний из которых завершен пламенем, и с поясом национального орнамента на обруче. \n'
                         '\n'
                         'Щитодержатели – два золотых медведя, '
                         'поддерживающие два золотых древка с Государственными флагами округа '
                         'на подножии из зелёных кедровых ветвей с шишками. \n'
                         '\n'
                         'Девиз «ДЕЛАМИ ВЕЛИКАЯ» начертан серебряными литерами на лазоревой ленте.')

        btn_crown = types.KeyboardButton('👑 Корона')
        btn_shield = types.KeyboardButton('🏵️ Щит')
        btn_bears = types.KeyboardButton('🐻 Медведи')
        btn_bird = types.KeyboardButton('🕊️ Птица')
        btn_flag = types.KeyboardButton('🚩 Флаг')
        btn_slogan = types.KeyboardButton('📯 Девиз')
        btn_back = types.KeyboardButton('📚 К разделам')
        markup.add(btn_crown, btn_shield, btn_bears, btn_bird, btn_flag, btn_slogan, btn_back)
        bot.send_message(message.from_user.id, '👇 Вы можете узнать подробнее о каждом элементе герба',
                         reply_markup=markup)

    elif message.text == '👑 Корона':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.from_user.id, 'Один из ярких элементов герба Югры - земельная корона о семи зубцах, '
                                               'распологающаяся на щите. '
                                               'На обруче короны национальный орнамент двух '
                                               'местных народов - ханты и манси. '
                                               'Венчает корону пламя, символизирующее нефтегазовый промысел региона.\n'
                                               '\n'
                                               'Почему же корона "земельная"?\n'
                                               '\n'
                                               'Согласно гербовнику Миниха (1730 г.), геральдические короны в '
                                               'Российской империи делились на несколько типов: \n'
                                               '\n'
                                               '• Императорскую\n'
                                               '• Царскую\n'
                                               '• Княжескую (Великокняжескую)\n'
                                               '• Земельную\n'
                                               '• Территориальную.\n'
                                               '\n'
                                               'Земельная корона даровалась губерниям и провинциям, не являвшимися '
                                               'в древности царством или княжеством, что соответствует '
                                               'статусу нашего округа.\n'
                                               '\n'
                                               'Подробнее про остальные типы корон можно прочитать по ссылке: '
                                               'https://sovet.geraldika.ru/article/8026/1/')

        btn_back_to_elements = types.KeyboardButton('🔍 К элементам')
        markup.add(btn_back_to_elements)
        bot.send_message(message.from_user.id, 'Чтобы вернуться к списку элеметов, нажмите "🔍 К элементам"',
                         reply_markup=markup)

    elif message.text == '🏵️ Щит':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.from_user.id, 'Важным элементом герба ХМАО-Югры является щит. Он разделён по середине '
                                               'вертикальной полосой на две части: синюю и зелёнюю. Эти два цвета '
                                               '(помимо белого) являются основными в символике региона. На щите '
                                               'располагается птица Кат ухуп вой. Венчает его земельная корона о семи '
                                               'зубцах. Щит на гербе '
                                               'округа имеет фигурную форму.\n'
                                               '\n'
                                               'Кстати о формах. Их всего 11 и они названы по национальной '
                                               'принадлежности рыцарства, предпочитавшего определённую конфигурацию '
                                               'щитов.\n'
                                               'Самым распространённым является "французский щит". Такую форму имеет, '
                                               'кстати, и герб России.\n'
                                               '\n'
                                               'Подробнее о формах щитов и их распространении здесь: '
                                               'https://ru.wikipedia.org/wiki/%D0%A9%D0%B8%D1%82_'
                                               '(%D0%B3%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%B4%D0%B8%D0%BA%D0%B0)')

        btn_back_to_elements = types.KeyboardButton('🔍 К элементам')
        markup.add(btn_back_to_elements)
        bot.send_message(message.from_user.id, 'Чтобы вернуться к списку элеметов, нажмите "🔍 К элементам"',
                         reply_markup=markup)

    elif message.text == '🐻 Медведи':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.from_user.id, 'На гербе округа расположены два золотых медведя, повёрнутые мордой к '
                                               'щиту. В лапах они держат флаг округа.\n'
                                               '\n'
                                               'Интересная информация:\n'
                                               '\n'
                                               'Оказывается, медведи на гербах встречаются исключительно в славянской '
                                               'и германской геральдический традициях. Причём в германской геральдике '
                                               'допускается только профильное изображение медведя, стоящего '
                                               'на двух лапах и повёрнутого вправо. В русской геральдике допускается '
                                               'медведь, идущий на четырёх лапах и влево.\n'
                                               '\n'
                                               'Различается также и символизм медведя. Если у германцев медведь - '
                                               'символ предусмотрительности, то в России - символ отдалённости и, '
                                               'конечно, севера (в южной России медведей нет).\n'
                                               '\n'
                                               'Более подробно можно прочитать здесь: '
                                               'https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B4%D0%B2%D0%B5%D0%B4%D1%'
                                               '8C_%D0%B2_%D0%B3%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%B4%D0%B8%D0%BA%D0%B5')

        btn_back_to_elements = types.KeyboardButton('🔍 К элементам')
        markup.add(btn_back_to_elements)
        bot.send_message(message.from_user.id, 'Чтобы вернуться к списку элеметов, нажмите "🔍 К элементам"',
                         reply_markup=markup)

    elif message.text == '🕊️ Птица':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.from_user.id, 'На щите герба ХМАО-Югры изображена священная для народов ханты и манси '
                                               'птица Кат ухуп вой. Она имеет две головы и четыре ноги с хвостом, '
                                               'подобным павлиньему. Фольклорное описание птицы гласит:\n'
                                               '"Его одно крыло — семь саженей, второе крыло — семь саженей. '
                                               'Мог целые сопки поднимать."\n'
                                               'Кат ухуп вой - поистине уникальный символ '
                                               'культуры '
                                               'Югры.\n'
                                               '\n'
                                               'Интересная информация:\n'
                                               '\n'
                                               'Птицы изображены на 35% всех государственных гербов. При этом '
                                               'половина из них содержит изображение орлов, соколов, ястребов и '
                                               'кондоров.\n'
                                               '\n'
                                               'Подробнее о птицах в геральдике можно прочитать здесь: '
                                               'https://ru.wikipedia.org/wiki/%D0%9F%D1%82%D0%B8%D1%86%D1%8B_%D0%B2_%D0'
                                               '%B3%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%B4%D0%B8%D0%BA%D0%B5')

        btn_back_to_elements = types.KeyboardButton('🔍 К элементам')
        markup.add(btn_back_to_elements)
        bot.send_message(message.from_user.id, 'Чтобы вернуться к списку элеметов, нажмите "🔍 К элементам"',
                         reply_markup=markup)

    elif message.text == '🚩 Флаг':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.from_user.id, 'Также на гербе Югры изображены флаги региона, которые держат в своих '
                                               'лапах медведи.\n'
                                               '\n'
                                               'Описание флага таково:\n'
                                               '\n'
                                               'Флаг Ханты-Мансийского автономного округа представляет собой '
                                               'прямоугольное полотнище, разделённое по горизонтали на две '
                                               'равновеликие полосы (верхняя — сине-голубая, нижняя — зелёная), '
                                               'завершённое по вертикали прямоугольной полосой белого цвета. '
                                               'В левой верхней части полотна расположен элемент белого цвета '
                                               'из герба Ханты-Мансийского автономного округа.\n'
                                               '\n'
                                               'Синий цвет флага символизирует водные ресурсы региона: '
                                               'около 30 тысяч рек и 290 тысяч озер. Зеленый цвет — символ бескрайней '
                                               'сибирской тайги. Белый цвет напоминает о суровой зиме и '
                                               'северных снегах, покрывающих территорию округа в течение семи '
                                               'календарных месяцев года. Сибирская корона в виде стилизованного '
                                               'изображения оленьих рогов — традиционный элемент национального '
                                               'орнамента народов ханты и манси, занимающихся оленеводством.')

        bot.send_photo(message.from_user.id, photo='https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/'
                                                   'Flag_of_Yugra.svg/1920px-Flag_of_Yugra.svg.png')

        btn_back_to_elements = types.KeyboardButton('🔍 К элементам')
        markup.add(btn_back_to_elements)
        bot.send_message(message.from_user.id, 'Чтобы вернуться к списку элеметов, нажмите "🔍 К элементам"',
                         reply_markup=markup)

    elif message.text == '📯 Девиз':
        markup = types.ReplyKeyboardMarkup()
        bot.send_message(message.from_user.id, 'В нижней части герба ХМАО-Югры расположен девиз "ДЕЛАМИ ВЕЛИКАЯ", '
                                               'взятый из гимна округа.\n'
                                               '\n'
                                               'Интересная информация:\n'
                                               '\n'
                                               'У российских императоров и императриц были девизы на некоторых '
                                               'печатях. Например, у Петра I девиз на одной из печатей гласит '
                                               '"DAT ET AUFFRT" '
                                               '(Дать и предложить - лат.), а на другой - "ADIUVANTE" '
                                               '(Помощь - лат.).\n'
                                               '\n'
                                               'Императрица Екатерина II для личной корресподенции использовала '
                                               'печать с девизом "СМЕРТЬ ЕДИНА МЯ РАЗВЯЖЕТ". Слово на частной печати - '
                                               '"ПОЛЕЗНОЕ".\n'
                                               '\n'
                                               'А Александр II стал первым русским императором, включившим в состав '
                                               'Императорского герба известный и по сей день девиз "С НАМИ БОГ".\n'
                                               '\n'
                                               'Подробнее про девизы на гербах можно прочитать по ссылке: '
                                               'https://cyberleninka.ru/article/n/status-slovesnogo-deviza-v-'
                                               'geraldicheskoy-sisteme/viewer')

        btn_back_to_elements = types.KeyboardButton('🔍 К элементам')
        markup.add(btn_back_to_elements)
        bot.send_message(message.from_user.id, 'Чтобы вернуться к списку элеметов, нажмите "🔍 К элементам"',
                         reply_markup=markup)

    elif message.text == '📚 К разделам':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('❓ Что такое геральдика?')
        btn2 = types.KeyboardButton('🦣 Геральдика ХМАО-Югры')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '👇 Выберите интересующий раздел', reply_markup=markup)

    elif message.text == '🔍 К элементам':
        markup = types.ReplyKeyboardMarkup()
        btn_crown = types.KeyboardButton('👑 Корона')
        btn_shield = types.KeyboardButton('🏵️ Щит')
        btn_bears = types.KeyboardButton('🐻 Медведи')
        btn_bird = types.KeyboardButton('🕊️ Птица')
        btn_flag = types.KeyboardButton('🚩 Флаг')
        btn_slogan = types.KeyboardButton('📯 Девиз')
        btn_back = types.KeyboardButton('📚 К разделам')
        markup.add(btn_crown, btn_shield, btn_bears, btn_bird, btn_flag, btn_slogan, btn_back)
        bot.send_message(message.from_user.id, '👇 Вы можете узнать подробнее о каждом элементе герба',
                         reply_markup=markup)

    else:
        markup = types.ReplyKeyboardMarkup()

        btn_back = types.KeyboardButton('📚 К разделам')
        markup.add(btn_back)

        bot.send_message(message.from_user.id, '🙁 Я Вас не понимаю. Рекомендую вернуться 📚 К разделам',
                         reply_markup=markup)


bot.polling(none_stop=True, interval=0)
