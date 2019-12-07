from cise import app


@app.route('/')
def hello_world():
    return 'Hello, World!!'

@app.route('/brandt')
def brandt_route():
    return 'welcome to my route'