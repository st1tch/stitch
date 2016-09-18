class TCPClient():
    SEND = 0b10
    RECV = 0b01

    def __init__(self, host, port, debug=None):
        if debug is None:
            debug = 0
        self.debug = debug
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.settimeout(10)
        self.sock.connect((host, port))
        self.sock.settimeout(None)

    def debug_log(self, size, data, cmd):
        if self.debug != 0:
            print "%s(%d): %s" % (cmd, size, repr(data))

    def send(self, data, delay=0):
        if delay:
            time.sleep(delay)
        nsend = self.sock.send(data)
        if self.debug & TCPClient.SEND:
            self.debug_log(nsend, data, "send")
        return nsend

    def sendline(self, data, delay=0):
        nsend = self.send(data + "\n", delay)
        return nsend

    def recv(self, size=1024, delay=0):
        if delay:
            time.sleep(delay)
        buf = self.sock.recv(size)
        if self.debug & TCPClient.RECV:
            self.debug_log(len(buf), buf, "recv")
        return buf

    def recv_until(self, regex_delim):
        buf = ""
        while True:
            c = self.sock.recv(1)
            buf += c
            if re.search(regex_delim, buf):
                break
        self.debug_log(len(buf), buf, "recv")
        return buf

    def recvline(self):
        buf = self.recv_until("\n")
        return buf

    def close(self):
        self.sock.close()
