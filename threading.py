import TestThreads

class sendMessage(TestThreads.Thread):
    def run(self):
        for _ in range(10):
            print(TestThreads.currentThread().getName())

x = sendMessage(name = 'Send message')
y = sendMessage(name = 'Receive message')
x.start()
y.start()