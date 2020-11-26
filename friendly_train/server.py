import asyncio
import getopt
import sys


async def push_pipe(reader, writer, preamble=">>>"):

    try:
        while not reader.at_eof():
            stuffs = await reader.read(2048)
            print(f"{preamble} {stuffs}")
            writer.write(stuffs)
    finally:
        writer.close()

def form_handle_client(client_machine, client_port):

    async def handle_client(local_reader, local_writer, client_port=80):
        try:
            remote_reader, remote_writer = await asyncio.open_connection('127.0.0.1', client_port)
            pipe1 = push_pipe(local_reader, remote_writer)
            pipe2 = push_pipe(remote_reader, local_writer, preamble="<<<")
            await asyncio.gather(pipe1, pipe2)
        finally:
            local_writer.close()

    return handle_client


def run_server(client_machine='127.0.0.1', client_port=80, host_port=8888):

    loop = asyncio.get_event_loop()
    srot = asyncio.start_server(form_handle_client(client_machine, client_port),
                                '127.0.0.1',
                                host_port)
    server = loop.run_until_complete(srot)

    # Bidirectional pipe with echo until interrupted

    print(f'### Serving on {server.sockets[0].getsockname()}')
    print(f"### Target {client_machine}:{client_port}")
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


def main(args):

    client_machine = '127.0.0.1'
    client_port = 80
    host_port = 8888

    opts, args = getopt.getopt(args,'m:p:h:')
    for opt, arg in opts:
        if opt == '-m':
            client_machine = arg
        if opt == '-p':
            client_port = int(arg)
        if opt == '-h':
            host_port = int(arg)
    run_server(client_machine, client_port, host_port)


if __name__ == '__main__':
    main(sys.argv[1:])
