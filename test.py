import json

import db_handlers

r = db_handlers.get_tenders_from_server('молоко')
js = json.loads(r)
print(js)
