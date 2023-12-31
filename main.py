import telebot
from telebot import types
import random

# Замените 'YOUR_TOKEN' на токен вашего бота
TOKEN = 'Токен Для бота'
bot = telebot.TeleBot(TOKEN)

facts = [
    'Специалисты по технологии блокчейна будут обеспечивать безопасность и прозрачность цифровых транзакций.',
    'Инженеры по созданию гиперзвуковых транспортных средств будут работать над развитием сверхбыстрых перевозок.',
    'Специалисты по киберфизическим системам будут интегрировать цифровые технологии с физическими процессами.',
    'Экологические архитекторы будут проектировать здания с использованием устойчивых и энергоэффективных технологий.',
    'Инженеры по созданию искусственных органов будут разрабатывать методы биопечати и трансплантации.',
    'Специалисты по этическому хакингу будут тестировать системы на безопасность, предотвращая кибератаки.',
    'Создатели контента для виртуальной реальности будут разрабатывать интерактивные сценарии и миры.',
    'Специалисты по антропоморфным роботам будут создавать роботов, имитирующих человеческое поведение и эмоции.',
    'Генетические консультанты будут помогать людям принимать информированные решения о своем генетическом коде.',
    'Специалисты по косметогенетике будут разрабатывать косметические продукты, учитывая индивидуальные генетические особенности.',
    'Инженеры по созданию беспилотных летательных аппаратов будут работать над технологиями автономной авиации.',
    'Специалисты по нанотехнологиям будут создавать материалы с уникальными свойствами на молекулярном уровне.',
    'Разработчики голографических технологий будут создавать трехмерные изображения для различных приложений.',
    'Специалисты по киберспорту будут тренировать профессиональных киберспортсменов в различных дисциплинах.',
    'Разработчики интеллектуальных транспортных систем будут работать над созданием умных городских транспортных сетей.',
    'Специалисты по восстановлению биоразнообразия будут заниматься восстановлением и охраной экосистем.',
    'Инженеры по созданию чистых источников энергии будут работать над альтернативными источниками энергии.',
    'Специалисты по технологиям хранения данных будут разрабатывать эффективные и безопасные методы хранения информации.',
    'Разработчики генетических тестов будут предоставлять персонализированную информацию о здоровье на основе генетического кода.',
    'Специалисты по технологии сквозного обучения будут создавать образовательные программы, интегрируя цифровые и физические опыты.',
    'Архитекторы атмосферных городов будут проектировать города в воздушном пространстве.',
    'Специалисты по кибертерапии будут использовать виртуальные технологии для лечения психологических расстройств.',
    'Инженеры по созданию домашних роботов будут разрабатывать умные устройства для автоматизации бытовых задач.',
    'Специалисты по агротехнологиям будут создавать инновационные методы сельского хозяйства и выращивания продуктов.',
    'Разработчики генетически модифицированных организмов будут трудиться над созданием более устойчивых и эффективных культур.',
    'Специалисты по кибергигиене будут разрабатывать технологии для поддержания здоровья в виртуальном пространстве.',
    'Инженеры по созданию экосистем в закрытом пространстве будут работать над созданием устойчивых биосфер на других планетах.',
    'Специалисты по робототехнике для медицины будут разрабатывать хирургических роботов и устройства для диагностики.',
    'Специалисты по криптовалютам будут управлять и развивать цифровые финансовые системы.',
    'Инженеры по созданию технологий очистки воды будут работать над методами обеспечения доступа к чистой воде в мире.',
    'Специалисты по биотехнологии пищи будут создавать искусственные продукты с улучшенными питательными характеристиками.',
    'Разработчики технологий виртуальной реабилитации будут использовать виртуальные миры для лечения и восстановления.',
    'Специалисты по персональной генетике будут предоставлять услуги по анализу генетической информации для заботы о здоровье.',
    'Архитекторы подводных городов будут создавать инфраструктуру для жизни и работы под водой.',
    'Специалисты по технологиям управления сном будут разрабатывать методы улучшения качества сна.',
    'Инженеры по созданию искусственного времени будут исследовать возможности изменения восприятия времени.',
    'Специалисты по динамической архитектуре будут создавать здания, способные менять свою форму и функцию в зависимости от потребностей.',
    'Нейросексологи будут разрабатывать технологии для улучшения сексуального опыта с использованием нейроинтерфейсов.',
    'Специалисты по психофармакологии будут разрабатывать новые методы воздействия на мозг для улучшения когнитивных функций.',
    'Архитекторы атмосферных городов будут создавать города в атмосфере, подвешенные в воздухе.',
    'Специалисты по генерации сновидений будут создавать искусственные сновидения для развлечения и творчества.',
    'Инженеры по созданию биоразлагаемых материалов будут работать над устойчивыми альтернативами пластиковым изделиям.',
    'Специалисты по технологиям экологического строительства будут использовать инновационные материалы и методы.',
    'Разработчики генетических технологий будут создавать методы редактирования генов для лечения наследственных заболеваний.',
    'Специалисты по космической археологии будут изучать артефакты и следы человеческой деятельности в космосе.',
    'Инженеры по созданию умных одежд будут интегрировать электронику для мониторинга здоровья и комфорта.']


# Вступительное сообщение
@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("▶️ЗАПУСТИТЬ▶️")
    markup.add(btn1)
    c = open('files/welcome.png', 'rb')
    bot.send_photo(message.chat.id, c, "Привет! Я бот «Город открытий». Чем я могу вам помочь?", reply_markup=markup)

# Обработка кнопки "Запустить"
@bot.message_handler(func=lambda message: True)
def get_text_messages(message):
    if message.text == '▶️ЗАПУСТИТЬ▶️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🗺Что такое «Город открытий»🗺")
        btn2 = types.KeyboardButton("🌏Какие маршруты есть в «Городе открытий»?🌏")
        btn3 = types.KeyboardButton("🛩Как отправиться в путешествие?🛩")
        btn4 = types.KeyboardButton("✅Кто может отправиться в путешествие?✅")
        btn5 = types.KeyboardButton("💸Как купить тур?💸")
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5)
        b = open('files/answer.png', 'rb')
        bot.send_photo(message.chat.id, b, "Выберите вопрос:", reply_markup=markup)

    elif message.text == '⬅️Назад⬅️':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🗺Что такое «Город открытий»🗺")
        btn2 = types.KeyboardButton("🌏Какие маршруты есть в «Городе открытий»?🌏")
        btn3 = types.KeyboardButton("🛩Как отправиться в путешествие?🛩")
        btn4 = types.KeyboardButton("✅Кто может отправиться в путешествие?✅")
        btn5 = types.KeyboardButton("💸Как купить тур?💸")
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5)
        d = open('files/answer.png', 'rb')
        bot.send_photo(message.chat.id, d, "выберите вопрос:", reply_markup=markup)

    elif message.text == '🗺Что такое «Город открытий»🗺':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️Назад⬅️')
        markup.add(btn1)
        a = open('files/what.png', 'rb')
        bot.send_photo(message.from_user.id, a, '«Город открытий» — это увлекательное и познавательное путешествие для школьников и студентов, это знакомство с инновационными отраслями, индустриями и профессиями будущего, возможность научиться открывать новые ресурсы в себе и находить их в пространстве города', reply_markup=markup)

    elif message.text == '🌏Какие маршруты есть в «Городе открытий»?🌏':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🌱Экология🌱')
        btn2 = types.KeyboardButton('🖌Креативные индустрии🖌')
        btn3 = types.KeyboardButton('🔬Биотехнологии и медицина🔬')
        btn4 = types.KeyboardButton('💻Цифровые технологии💻')
        btn5 = types.KeyboardButton('🚗Транспорт и космос🚗')
        btn6 = types.KeyboardButton('🎓Гуманитарные технологии🎓')
        btn7 = types.KeyboardButton('🏙Урбанистика🏙')
        btn8 = types.KeyboardButton('💡Энергетика💡')
        btn9 = types.KeyboardButton('⬅️Назад⬅️')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        a = open('files/navig.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Какой маршрут интересен тебе?', reply_markup=markup)

    elif message.text == '🛩Как отправиться в путешествие?🛩':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️Назад⬅️')
        markup.add(btn1)
        a = open('files/kak.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Тебе нужно падать заявку на нашем сайте https://городоткрытий.рф/. Там же ищи подробности, если что-то непонятно', reply_markup=markup)
        random_fact = random.choice(facts)
        bot.send_message(message.chat.id, f"Интересный факт: {random_fact}")

    elif message.text == '✅Кто может отправиться в путешествие?✅':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️Назад⬅️')
        markup.add(btn1)
        a = open('files/kto.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Классы из всех школ России, подробности на https://городоткрытий.рф/. ', reply_markup=markup)

    elif message.text == '💸Как купить тур?💸':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️Назад⬅️')
        markup.add(btn1)
        a = open('files/tur.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Заказать тур вы можете на нашем сайте - ' + 'https://городоткрытий.рф/.', reply_markup=markup)

    elif message.text == '🌱Экология🌱':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️Назад⬅️')
        markup.add(btn1)
        a = open('files/eko.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Человек — это вид, который за несколько тысячелетий изменил окружающую среду больше, чем это сделали все остальные биологические виды планеты вместе взятые. И сегодня эти изменения угрожают выживанию самого человека.', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Экология — это отрасль, призванная сохранить экосистемы планеты. Экология изучает влияние деятельности человека на окружающую среду и принимает меры, чтобы уменьшить ее негативное влияние и последствия.', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Перед отраслью стоят важнейшие вопросы: как преодолеть истощение почв, загрязнение мирового океана? Как организовать безотходное производство? Как эффективно использовать и перерабатывать отходы?', reply_markup=markup)
        random_fact = random.choice(facts)
        bot.send_message(message.chat.id, f"Интересный факт: {random_fact}")

    elif message.text == '🖌Креативные индустрии🖌':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️Назад⬅️')
        markup.add(btn1)
        a = open('files/cre.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Креативные индустрии стирают грань между фантазией и реальным миром. Это архитектура, искусство и культура, ремесла, дизайн, мода, музыка, литература и издательское дело, кино, телевидение, реклама.', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Ключевой объединяющий фактор для всех этих культурных практик — это доминирование креативной, творческой составляющей, нацеленность на то, чтобы создавать нечто, не существовавшее ранее.', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Креативные индустрии не просто следуют трендам, они создают их.', reply_markup=markup)
        random_fact = random.choice(facts)
        bot.send_message(message.chat.id, f"Интересный факт: {random_fact}")

    elif message.text == '🔬Биотехнологии и медицина🔬':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️Назад⬅️')
        markup.add(btn1)
        a = open('files/med.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Биотехнологии — активно развивающаяся отрасль, ищущая новые возможности использования биологических систем и процессов. Она включает в себя несколько десятков различных направлений на стыке биологии, химии и технических наук.', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Сегодня в сегменте медицины перспективные разработки ведутся в направлении редактирования генома и генной терапии, разработке биосовместимых имплантов, создания лекарств и вакцин нового поколения.', reply_markup=markup)
        bot.send_message(message.from_user.id, 'В промышленном сегменте биотехнологий приоритетными областями являются получение биополимеров и биотоплива, а в аграрном сегменте передовые исследования ведутся в направлении создания новых сортов растений и пород животных с заданными свойствам и производство биопрепаратов для растениеводства и ветеринарии.', reply_markup=markup)
        random_fact = random.choice(facts)
        bot.send_message(message.chat.id, f"Интересный факт: {random_fact}")

    elif message.text == '💻Цифровые технологии💻':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️Назад⬅️')
        markup.add(btn1)
        a = open('files/robo.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'IT — это одна из самых быстро развивающихся отраслей в мире.', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Это технологии сбора и обработки информации, создание новых программ и приложений, цифровых устройств и средств связи.', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Сегодня цифровые технологии пронизывают всю нашу повседневную жизнь. А уже завтра обыденными станут новые возможности — Интернет вещей, бытовые роботы, дополненная и виртуальная реальность, нейронные сети и искусственный интеллект', reply_markup=markup)
        random_fact = random.choice(facts)
        bot.send_message(message.chat.id, f"Интересный факт: {random_fact}")

    elif message.text == '🚗Транспорт и космос🚗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️Назад⬅️')
        markup.add(btn1)
        a = open('files/sky.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Человечество становится все более мобильным. За месяц мы преодолеваем расстояние больше, чем наши деды проезжали за всю жизнь. Сегодня мы путешествуем не только между городами и континентами. Люди могут покидать родную планету и вновь возвращаться домой. Мы уже побывали на Луне и, как говорят ученые, уже скоро полетим на Марс. Такие возможности перед нами открывают транспортные и космические технологии.', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Скорости наших перемещений возросли в тысячи раз и со временем будут только расти. Вместе с этим будет увеличиваться и безопасность транспортных перевозок.', reply_markup=markup)
        bot.send_message(message.from_user.id, 'В ближайшем будущем индустрия транспорта подарит человечеству умные дороги, беспилотные автомобили, межпланетные космические корабли, а также новые средства передвижения по нашей родной планете.', reply_markup=markup)
        random_fact = random.choice(facts)
        bot.send_message(message.chat.id, f"Интересный факт: {random_fact}")

    elif message.text == '🎓Гуманитарные технологии🎓':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️Назад⬅️')
        markup.add(btn1)
        a = open('files/teh.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Эта отрасль объединяет самые человеческие технологии. Сюда относятся образование, социальная помощь и защита, психология, менеджмент, социология, антропология, политология и многие другие.', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Это области профессиональной деятельности, центральным фокусом которых является человек, человеческие отношения и общности. Они относятся к самым разным группам людей - семья, команда, организация, корпорация, государство, этнос и человеческая цивилизация в целом.', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Гуманитарные технологии нацелены на создание условий для всестороннего развития личности, преобразование общества в открытое перспективное пространство согласно вызовам современности.', reply_markup=markup)
        random_fact = random.choice(facts)
        bot.send_message(message.chat.id, f"Интересный факт: {random_fact}")

    elif message.text == '🏙Урбанистика🏙':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️Назад⬅️')
        markup.add(btn1)
        a = open('files/urb.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Урбанистика - это относительно молодая отрасль, в которой работают представители самых разных профессий – технических, творческих и гуманитарных. Эти специалисты объединяют свои усилия, чтобы сделать современные города комфортными для проживания.', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Как учесть образ жизни горожан и их потребности при строительстве? Как вписать новые здания и сооружения в существующий ландшафт? Где расположить и как оборудовать транспортные узлы и зоны отдыха, как создать оптимальное транспортное сообщение, чтобы всем горожанам было удобно? На эти и многие другие вопросы призвана ответить урбанистика.', reply_markup=markup)
        random_fact = random.choice(facts)
        bot.send_message(message.chat.id, f"Интересный факт: {random_fact}")

    elif message.text == '💡Энергетика💡':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⬅️Назад⬅️')
        markup.add(btn1)
        a = open('files/ener.png', 'rb')
        bot.send_photo(message.from_user.id, a, 'Наша цивилизация становится все более энергоемкой. Обыденная жизнь каждого человека связана с постоянным энергопотреблением. Новые технологии и производства требуют новых источников энергии. При этом многие традиционные источники энергии иссякают, и добывать их становится все сложнее.', reply_markup=markup)
        bot.send_message(message.from_user.id, 'Перед человечеством стоит задача поиска новых источников энергии и эффективных технологий ее передачи и сохранения. В ближайшее время энергетическая отрасль создаст такие инновационные решения, как атмосферная электроэнергеткика, холодный ядерный синтез, беспроводная передача электричества.', reply_markup=markup)

        random_fact = random.choice(facts)
        bot.send_message(message.chat.id, f"Интересный факт: {random_fact}")


# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
