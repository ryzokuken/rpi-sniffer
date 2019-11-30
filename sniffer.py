def print_callback(pkt):
    print 'Just arrived:', pkt

capture = pyshark.LiveCapture(interface='eth0')
capture.sniff(timeout=50)
capture.apply_on_packets(print_callback, timeout=5)

