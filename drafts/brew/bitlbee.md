---
name: bitlbee
title: BitlBee
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, chat, gateway, irc, old-school, protocol, xmpp]
homepage: https://www.bitlbee.org/
scout_score: 5
status: draft
---

# BitlBee

**TLDR;** An IRC server that turns your instant-messaging accounts into IRC nicks and channels, so any IRC client can talk XMPP, Twitter and more.

BitlBee is an IRC daemon that does not host chat itself. You run it locally, point an ordinary IRC client at it, and it logs into your other chat accounts on your behalf. Your contacts appear as IRC nicks, and group chats appear as channels. You talk to people by opening a query, or by typing `nick: text` in the control channel.

When you connect you are placed in a channel called &bitlbee, where a bot user named root answers commands. That channel is the whole interface for managing accounts. You register with a password so your settings and contacts are saved on the server, add an account, switch it on, and your buddy list fills in as people in the channel.

The homepage says it exists for 'people who have an IRC client running all the time and don't want to run an additional XMPP/facebook/discord/whatever client.' The idea underneath is the gateway: take one protocol and present it as another, so a single client can cover many networks. It shows how much of chat (presence, queries, group rooms) maps onto IRC's old model, and where the mapping gets awkward.

Only Jabber/XMPP and Twitter are built in. Other networks come from plugins such as facebook, discord, steam and mastodon, or through libpurple. The project's news posts are candid about protocols dying off, and the 3.4.2 post puts it this way: 'you just have to appreciate the beauty of things that are imperfect, impermanent and incomplete.'

## Install

```
brew install bitlbee
# You also need an IRC client. The brief did not cover Brew-specific setup; the user guide describes a source build (./configure, make, make install) with its config directory defaulting to /var/lib/bitlbee.
```

## Try this

```
register <password>
```
Run in &bitlbee after connecting your IRC client to localhost port 6667. It saves your passwords, contacts and settings on the BitlBee server.

```
account add <protocol> <username> [<password>]
```
Adds an IM account, for example a Jabber/XMPP one. The password can be left out and entered separately.

```
account on
```
Logs into your accounts, and your contacts begin appearing in the control channel as IRC users.

## What's unique

It is a 2000s-style protocol gateway that still works, with a bot-run buddy list channel and group chats that look like IRC channels. Few tools make the mapping between two chat protocols this visible.

## Caveats

The last stable release is 3.6 from February 2019, though the git tree has activity through 2025; the 3.6 release removed MSN, Skype and ICQ/AIM, and the user guide itself warns it can crash or corrupt data and is partly outdated.

## Links

- [BitlBee homepage](https://www.bitlbee.org/)
- [BitlBee User Guide (partly outdated)](https://www.bitlbee.org/main.php/user-guide.html)
