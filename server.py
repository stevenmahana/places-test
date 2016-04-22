import time
import zmq

class Places(object):

    @staticmethod
    def receive_message():

        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:5556")

        while True:
            #  Wait for next request from client
            message = socket.recv()
            print("Received request: %s" % message)

            #  Do some 'work'
            time.sleep(1)

            #  Send reply back to client
            socket.send(b"Places World")

if __name__ == '__main__':
    zs = Places()
    zs.receive_message()