from flask import Flask , redirect
from pyairtable import Table
    
app = Flask(__name__)

@app.route('/<id>')
def index(id):
    ids = []
    urls = []
    table = Table('keynabsTSGt63GDEw', 'appobl90u3RKofhha', 'urls')
    for j in table.all():
        ids.append((j['fields']['ID']).strip())
    for k in table.all():
        urls.append((k['fields']['URL']).strip())
    if id in ids:
        return redirect(("http://"+urls[ids.index(id)]), code=302)
    
if __name__ == '__main__':
    app.run()

