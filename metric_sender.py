import time
import socket
import metric_pb2

LO = '127.0.0.1'
PORT = 12435

def build_metric():
    """Builds a metric by protobuf

    Returns:
        Metric: Pythonic handler of the metric
    """

    protobuf_metric = metric_pb2.Metric()
    protobuf_metric.name = 'sys.cpu'
    protobuf_metric.type = 'gauge'
    protobuf_metric.value = 99.9
    protobuf_metric.tags.extend(['my_tag', 'foo:bar'])

    return protobuf_metric


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = build_metric().SerializeToString()
    
    s.sendto(packet, (LO, PORT))

    s.close()


if __name__ == '__main__':
    main()
