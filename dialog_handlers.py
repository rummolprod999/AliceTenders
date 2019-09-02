import suggests as s


sessionStorage = {}


def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new']:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.

        sessionStorage[user_id] = {
            'suggests': [
                "Продолжить",
                "Отказаться",
            ],
            'suggests_t': [
                "Искать",
                "Закончить",
            ]

        }

        res['response'][
            'text'] = 'Здравствуйте! Здесь вы можете найти актуальные тендеры с более чем 300 площадок России и зарубежья! Хотите продожить?'
        res['response']['buttons'] = s.get_first_suggests(user_id)
        return

    if start_dialog(req, res, user_id):
        return

    if end_dialog(req, res):
        return
    if find_tenders(req, res):
        return
    if select_req(req, res, user_id):
        return
    res['response']['text'] = 'Извините, не могу понять вопрос.'


def start_dialog(req, res, user_id):
    if req['request']['original_utterance'].lower() in [
        'продолжить',
        'хорошо',
        'продолжай',
        'давай',
        'ок',
        'да',
    ] or req['request']['command'] == 'Продолжить':
        res['response']['text'] = 'По какому запросу вас интересуют тендеры?'
        return True
    return False


def end_dialog(req, res):
    if req['request']['command'] == 'Отказаться' or req['request']['command'] == 'Закончить' or req['request'][
        'original_utterance'].lower() in [
        'отказаться',
        'не хочу',
        'не надо',
        'хватит',
        'отвали',
        'стоп',
        'нет',
        'закончить'
    ]:
        res['response']['text'] = 'Хорошо! Ждем вас в другой раз'
        res['response']['end_session'] = True
        return True
    return False


def select_req(req, res, user_id):
    if req['request']['command'] and not res['session']['new']:
        res['response']['text'] = 'Искать тендеры по запросу {}?'.format(
                req['request']['command'])
        res['response']['buttons'] = s.get_first_suggests_t(user_id)
        return True
    return False


def find_tenders(req, res):
    if (req['request']['command'] == 'Искать' or req['request'][
        'original_utterance'].lower() in [
            'искать',
            'найти',
            'поиск',
            'ищи',
            'найди',
            'поищи',
            'искать тендеры',
            'поищи']):
        res['response']['text'] = 'Нашел тенедры по запросу {}'.format(
                req['request']['original_utterance'])
        return True
    return False
