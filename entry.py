import web
from ConfigParser import ConfigParser

config = ConfigParser()
config.read('config.ini')

urls = (
    '/entry', 'entry',
    '/form', 'form',
)

#web.config.db_parameters = dict(dbn='sqlite', db='ttsrobot.db', user='', pw='')
db = web.database(dbn='sqlite', db=config.get('db', 'name'))
db.ctx.db.text_factory = str

class entry:
    
    def POST(self):
        entry = web.data()
        if entry:
            print 'data:', entry
            db.insert('jobs', value=entry)
        return ""

class form:

    def POST(self):
        entry = web.input()
        if entry and entry.content:
            print 'data:', entry.content.encode('utf-8')
            db.insert('jobs', value=entry.content)
        return ""


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
