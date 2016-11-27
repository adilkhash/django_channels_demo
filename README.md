# django_channels_demo
Demonstration of Django Channels using WebSocket

Please, follow this commands::
  python manage.py migrate

  redis-server

  daphne blog_channels.asgi:channel_layer --port 8000

  python manage.py runworker -v2
