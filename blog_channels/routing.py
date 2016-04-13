from channels.routing import route


channel_routing = {
    'websocket.connect': 'chat.consumers.ws_connect',
    'websocket.receive': 'chat.consumers.ws_message',
    'websocket.disconnect': 'chat.consumers.ws_disconnect',
}
