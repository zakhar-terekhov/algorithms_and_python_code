# использование селектора для построения неблокирующего сервера
import selectors
import socket
from selectors import SelectorKey

selector = selectors.DefaultSelector()

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.setblocking(False)  # пометить серверный сокет как неблокирующий
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events = selector.select(timeout=1)
    print(events)

    if len(events) == 0:
        print("Событий нет, жду еще")
    else:
        for event, _ in events:
            event_socket = (
                event.fileobj
            )  # получить сокет, для которого произошло событие

            if (
                event_socket == server_socket
            ):  # если событие произошло с серверным сокетом, значит была попытка подключ-я
                connection, client_address = server_socket.accept()
                connection.setblocking(
                    False
                )  # пометить клиентский сокет как неблокирующий
                print(f"Получен запрос на подключение от {client_address}")
                selector.register(
                    connection, selectors.EVENT_READ
                )  # зарегистировать клиент, подключившийся к сокету
            else:  # если событие произошло не с серверным сокетом, то получить данные от клиента и отправить их обратно
                data = event_socket.recv(1024)
                print(f"Получены данные: {data}")
                event_socket.send(data)
