from ModuleB import second
from threading import Thread

thread = Thread(target=second)
thread.start()
print('First')
