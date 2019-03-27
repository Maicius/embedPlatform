# Usage:

- XMPP服务器：nju-forum.top

- 客户端账号（jabber id）：romeo@nju-forum.top
- 客户端密码：1234

- 服务客户端账号（jabber id）：juliet@nju-forum.top
- 服务客户端密码：1234

- client:

        ./xmpp_bot.py -d -j romeo@nju-forum.top -p 1234 -t juliet@nju-forum.top

- server:

        ./xmpp_service.py -d -j juliet@nju-forum.top -p 1234
