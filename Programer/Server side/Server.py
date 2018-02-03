while 1:
    from multiprocessing.connection import Listener
    print "restarting ..."
    address = ('192.168.253.101', 6001)     # family is deduced to be 'AF_INET'
    listener = Listener(address, authkey='iLikeFatCats! bc8719873v4yb9c8yc8n2b98c927b618v7c8')
    conn = listener.accept()
    print 'connection accepted from', listener.last_accepted
    while True:
        try:
            msg = conn.recv()
            print msg
            # do something with msg
            if msg == 'close':
                conn.close()
                break
            if msg == 'open':
                print "Open"
        except:
            break
    listener.close()
