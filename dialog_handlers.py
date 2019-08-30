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
            ]
        }

        res['response'][
            'text'] = 'Здравствуйте! Здесь вы можете найти актуальные тендеры с более чем 300 площадок России и зарубежья! Хотите продожить?'
        res['response']['buttons'] = s.get_first_suggests(user_id)
        return

    if start_dialog(req, res):
        return
    if end_dialog(req, res):
        return

    res['response']['text'] = 'Извините, не могу понять вопрос.'


def start_dialog(req, res):
    if req['request']['original_utterance'].lower() in [
        'продолжить',
        'хорошо',
        'давай',
        'ок',
        'да',
        'продолжай',
    ] or req['request']['command'] == 'Продолжить':
        res['response']['text'] = 'По какому запросу вас интересуют тендеры?'
        return True
    return False


def end_dialog(req, res):
    if req['request']['command'] == 'Отказаться' or req['request']['original_utterance'].lower() in [
        'отказаться',
        'не хочу',
        'не надо',
        'хватит',
        'отвали',
        'стоп',
        'нет'
    ]:
        res['response']['text'] = 'Хорошо! Ждем вас в другой раз'
        res['end_session'] = True
        return True
    return False
