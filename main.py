import redis
import integration_pb2
from google.protobuf.json_format import MessageToJson, Parse

# Conectar a Redis
r = redis.Redis(host='192.168.0.123', port=6379, db=0)

# Nombre del stream específico del dispositivo
stream_name = 'device:stream:event'


# Leer los eventos del stream
def read_stream():
    last_id = '0-0'
    while True:
        events = r.xread({stream_name: last_id}, block=0, count=1)
        for event in events:
            mensaje = integration_pb2.UplinkEvent()
            mensaje.ParseFromString(event[1][0][1][b'up'])
            #event[1][0][1][b'up']
            json_str = MessageToJson(mensaje)
            print("Mensaje en JSON:", json_str)
            print('--------------------')
            print(event[1][0][1][b'up'])


if __name__ == "__main__":
    read_stream()
