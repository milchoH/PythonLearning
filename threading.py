import threading

class sendMessage(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = sendMessage(name = 'Send message')
y = sendMessage(name = 'Receive message')
x.start()
y.start()