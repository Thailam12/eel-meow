import eel

eel.init('templates')

@eel.expose
def get_log():
    return 0

eel.start('index.html', size=(800, 600))