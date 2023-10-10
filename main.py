from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cred import TOKEN
from menu import (
    main_menu_keyboard,
    courses_menu_keyboard
    )
from key_buttons import tele_buttons
from key_buttons import courses

ABOUT = tele_buttons[0]
COURSES = tele_buttons[1]
WE_ARE = tele_buttons[2]
PYTHON = courses[0]
JAVA = courses[1]
JAVAS = courses[2]
QA = courses[3]
BACK = courses[4]
def start(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Welcome {update.effective_user.username}',
        reply_markup=main_menu_keyboard()
    )
def about(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Преимущества обучения в Codify.'
         'Обучение с нуля до Junior. Пройди обучение по авторской программе Codify и стань Junior специалистом.',
    )
def reply_courses(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'О курсах',
         reply_markup=courses_menu_keyboard()
    )

def python_reply(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Python (МФА: [ˈpʌɪθ(ə)n]; в русском языке встречаются названия пито́н[24] или па́йтон[25]) — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью[26][27], ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ[28]. Язык является полностью объектно-ориентированным в том плане, что всё является объектами[26]. Необычной особенностью языка является выделение блоков кода пробельными отступами[29]. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации[28]. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[26]. Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++[26][28].'
        '\nPython является мультипарадигменным языком программирования, поддерживающим императивное, процедурное, структурное, объектно-ориентированное программирование[26], метапрограммирование[30] и функциональное программирование[26]. Задачи обобщённого программирования решаются за счёт динамической типизации[31][32]. Аспектно-ориентированное программирование частично поддерживается через декораторы[33], более полноценная поддержка обеспечивается дополнительными фреймворками[34]. Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек или расширений[35]. Основные архитектурные черты — динамическая типизация, автоматическое управление памятью[26], полная интроспекция, механизм обработки исключений, поддержка многопоточных вычислений с глобальной блокировкой интерпретатора (GIL)[36], высокоуровневые структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, могут объединяться в пакеты[37].',
    )
def java_reply(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Java[прим. 1] — строго типизированный объектно-ориентированный язык программирования общего назначения, разработанный компанией Sun Microsystems (в последующем приобретённой компанией Oracle). Разработка ведётся сообществом, организованным через Java Community Process; язык и основные реализующие его технологии распространяются по лицензии GPL. Права на торговую марку принадлежат корпорации Oracle.'
        'Приложения Java обычно транслируются в специальный байт-код, поэтому они могут работать на любой компьютерной архитектуре, для которой существует реализация виртуальной Java-машины. Дата официального выпуска — 23 мая 1995 года. Занимает высокие места в рейтингах популярности языков программирования (2-е место в рейтингах IEEE Spectrum (2020)[3] и TIOBE (2021)[4]).'
        
    )
def java_s_reply(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'JavaScript (/ˈdʒɑːvɑːˌskrɪpt/; аббр. JS /ˈdʒeɪ.ɛs./) — мультипарадигменный язык программирования. Поддерживает объектно-ориентированный, императивный и функциональный стили. Является реализацией спецификации ECMAScript (стандарт ECMA-262[8]).'

'JavaScript обычно используется как встраиваемый язык для программного доступа к объектам приложений. Наиболее широкое применение находит в браузерах как язык сценариев для придания интерактивности веб-страницам[9].'

'Основные архитектурные черты: динамическая типизация, слабая типизация, автоматическое управление памятью, прототипное программирование, функции как объекты первого класса.'

'На JavaScript оказали влияние многие языки, при разработке была цель сделать язык похожим на Java. Языком JavaScript не владеет какая-либо компания или организация, что отличает его от ряда языков программирования, используемых в веб-разработке[~ 1][10].'

'Название «JavaScript» является зарегистрированным товарным знаком корпорации Oracle в США[11].'

'В 1992 году компания Nombas (впоследствии приобретённая Openwave[en]) начала разработку встраиваемого скриптового языка Cmm (Си-минус-минус), который, по замыслу разработчиков, должен был стать достаточно мощным, чтобы заменить макросы, сохраняя при этом схожесть с Си, чтобы разработчикам не составляло труда изучить его[12]. Главным отличием от Си была работа с памятью. В новом языке всё управление памятью осуществлялось автоматически: не было необходимости создавать буфера, объявлять переменные, осуществлять преобразование типов. В остальном языки сильно походили друг на друга: в частности, Cmm поддерживал стандартные функции и операторы Си[13]. Cmm был переименован в ScriptEase, поскольку исходное название звучало слишком негативно, а упоминание в нём Си «отпугивало» людей[12][14]. На основе этого языка был создан проприетарный продукт CEnvi. В конце ноября 1995 года Nombas разработала версию CEnvi, внедряемую в веб-страницы. Страницы, которые можно было изменять с помощью скриптового языка, получили название Espresso Pages — они демонстрировали использование скриптового языка для создания игры, проверки пользовательского ввода в формы и создания анимации. Espresso Pages позиционировались как демоверсия, призванная помочь представить, что случится, если в браузер будет внедрён язык Cmm. Работали они только в 16-битовом Netscape Navigator под управлением Windows[15].'

'Самая первая реализация JavaScript была создана Бренданом Эйхом (англ. Brendan Eich) в компании Netscape, и с тех пор обновляется, чтобы соответствовать ECMA-262 Edition 5 и более поздним версиям. Этот движок называется SpiderMonkey и реализован на языке C/C++. Движок Rhino создан Норрисом Бойдом (англ. Norris Boyd) и реализован на языке Java. Как и SpiderMonkey, Rhino соответствует ECMA-262 Edition 5.'
    )
def QA_reply(update:Update, context:CallbackContext):
    update.message.reply_text(f'Тести́рование програ́ммного обеспе́че́ния — процесс исследования, испытания программного продукта, имеющий своей целью проверку соответствия между реальным поведением программы и её ожидаемым поведением на конечном наборе тестов, выбранных определённым образом'
    )
def back_reply(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Main Menu',
        reply_markup=main_menu_keyboard())
def location(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'У нас существуют два филиала расположенные на ​7-й микрорайон, 23 https://2gis.kg/bishkek/firm/70000001063954838'
        'А также на Улица Насирдина Исанова, 105/3, https://2gis.kg/bishkek/firm/70000001038163168 ',
    )

updater = Updater(token=TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSES),
    reply_courses
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON),
    python_reply
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JAVA),
    java_reply
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JAVAS),
    java_s_reply
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(QA),
    QA_reply
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    back_reply
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(WE_ARE),
    location
))
updater.start_polling()
updater.idle()