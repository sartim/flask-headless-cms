from skeleton.app import app

@app.route('/')
def root():
    return "Welcome!"
