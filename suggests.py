import dialog_handlers as dh


def get_first_suggests(user_id):
    session = dh.sessionStorage[user_id]
    suggests = [
        {'title': suggest, 'hide': True}
        for suggest in session['suggests'][:]
    ]

    return suggests
