import time
import socket
import metric_pb2

LO = '127.0.0.1'
PORT = 12435

def build_metric():
    """Builds a metric with protobuf.

    Returns:
        Metric: A populated Metric instance.
    """

    protobuf_metric = metric_pb2.TestMessage()
    protobuf_metric.length = 10
    protobuf_metric.dst = "Chandler Bing"
    protobuf_metric.src = "Joey Tribbiany"
    protobuf_metric.transid = 1337

    protobuf_metric.request.authToken = 'Friends'
    protobuf_metric.request.subscribe.unsubscribe = 0

    protobuf_metric.notfound = 'True'

    return protobuf_metric


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = build_metric().SerializeToString()
    
    s.sendto(packet, (LO, PORT))

    s.close()


if __name__ == '__main__':
    main()
