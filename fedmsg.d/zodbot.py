import socket
hostname = socket.gethostname()

config = dict(
    endpoints={
        "supybot.%s" % hostname: [
            "tcp://127.0.0.1:6009",
            "tcp://127.0.0.1:6010",
            "tcp://127.0.0.1:6011",
            "tcp://127.0.0.1:6012",
        ],
    },
)
