# Fundamentals you never look at twice

Protocols and plumbing that run all day in every house and nobody looks at. UPnP, SOAP, mDNS, ARP, DHCP, DNS internals, TLS handshakes. The entry is a door into the protocol, the tool is the key.

178 entries. [Back to the shelf](README.md)

## quick

- **[arping](../drafts/brew/arping.md)**: Asks the local network who owns an IP address by sending ARP requests, and can also ping a raw MAC address to find out which IP it uses.  
  `arp, network, protocol, root-needed`
- **[Avahi](../drafts/brew/avahi.md)**: Avahi is the Linux implementation of mDNS and DNS-SD, the Bonjour-style protocols that let machines announce and find printers, shares and .local names.  
  `dns-sd, linux, mdns, network, protocol, zeroconf`
- **[bgpq4](../drafts/brew/bgpq4.md)**: Turns Internet Routing Registry data into router filter configs, a way to see how the internet decides which networks to believe.  
  `bgp, irr, network, protocol, routing`
- **[bittwist](../drafts/brew/bittwist.md)**: A libpcap packet generator and capture editor that rewrites header fields in .pcap files and replays them onto a live network at a set rate.  
  `ethernet, network, packets, pcap, protocol`
- **[bitwise](../drafts/brew/bitwise.md)**: A terminal calculator that shows one number in every base at once and lets you toggle individual bits, with datasheet-style bit-field selects.  
  `bits, calculator, embedded, ncurses, tui`
- **[cdpr](../drafts/brew/cdpr.md)**: Listens for the Cisco Discovery Protocol chatter your switch already broadcasts and tells you which switch and port your machine is plugged into.  
  `cdp, cisco, network, pcap, protocol`
- **[certgraph](../drafts/brew/certgraph.md)**: Give it one hostname and it follows the names inside TLS certificates from site to site, building a graph of domains that share certificates.  
  `certificates, dns, network, protocol, tls`
- **[dhcpdump](../drafts/brew/dhcpdump.md)**: A packet decoder that shows the DHCP conversation on your network, with a full-screen view that groups traffic by client and labels each lease's state.  
  `dhcp, network, packet-capture, protocol`
- **[dict](../drafts/brew/dict.md)**: A command-line client for RFC 2229, the old dictionary protocol, with a live public server and tools to host or build your own dictionaries.  
  `ancient, dictionary, network, protocol, rfc`
- **[dnstop](../drafts/brew/dnstop.md)**: A tcpdump-style console tool that turns DNS packets into live ranked tables of who is asking for what, and which queries look wrong.  
  `dns, network, pcap, protocol, tui`
- **[dnstracer](../drafts/brew/dnstracer.md)**: Walks the DNS delegation chain from the root servers down to the authoritative one, printing every server it asks along the way.  
  `debugging, dns, network, protocol`
- **[dnstwist](../drafts/brew/dnstwist.md)**: Give it a domain and it generates lookalike typo and homoglyph variants, then checks which ones are actually registered and what they serve.  
  `dns, phishing, python, security, unicode`
- **[dumbpipe](../drafts/brew/dumbpipe.md)**: A netcat-style tool that pipes stdin and stdout between two machines anywhere, addressed by a long key instead of an IP address.  
  `nat-traversal, network, pipes, protocol, quic`
- **[endlessh](../drafts/brew/endlessh.md)**: An SSH tarpit that listens on a port and drips an endless, random banner to anything that connects, leaving bots stuck for hours.  
  `network, protocol, security, ssh, tarpit`
- **[GUPnP Tools](../drafts/brew/gupnp-tools.md)**: Six GNOME-hosted tools for finding UPnP devices on your network and poking at them, built as free replacements for Intel's UPnP tools.  
  `discovery, gui, network, protocol, upnp`
- **[hashcash](../drafts/brew/hashcash.md)**: A 1997 proof-of-work stamp: burn some CPU to mint it, check it with one hash. The idea behind Bitcoin mining, in its original small form.  
  `hashing, math, proof-of-work, protocol, spam`
- **[htpdate](../drafts/brew/htpdate.md)**: Sets your computer's clock from the Date headers of ordinary web servers, a way to keep time over HTTP without NTP.  
  `http, network, protocol, time`
- **[ldapvi](../drafts/brew/ldapvi.md)**: ldapvi pulls entries from an LDAP directory into your text editor and writes your edits back on save, like vipw for LDAP.  
  `editor, ldap, protocol, tui`
- **[lft](../drafts/brew/lft.md)**: A traceroute that works at the transport layer, aimed at tracing paths through networks where ordinary traceroute probes get dropped, and it ships a second tool, whob.  
  `network, protocol, tcp, traceroute`
- **[libnatpmp](../drafts/brew/libnatpmp.md)**: A small C client library, plus the natpmpc tool, for NAT-PMP: the protocol that lets a program ask your router for its public address and an open port.  
  `c, nat, network, protocol, router`
- **[librsync](../drafts/brew/librsync.md)**: The rsync delta algorithm as a C library, plus rdiff, a tool that makes a patch from a tiny checksum file instead of the old file itself.  
  `backup, checksums, delta, library, rsync`
- **[lrzsz](../drafts/brew/lrzsz.md)**: Send and receive files over a serial line or terminal session with XMODEM, YMODEM and ZMODEM, the pre-network protocols that once moved files between machines.  
  `ancient, file-transfer, protocol, serial, zmodem`
- **[magic-wormhole](../drafts/brew/magic-wormhole.md)**: Send a file between two computers by reading a short code aloud, with end-to-end encryption and no accounts or shared server.  
  `cli, cryptography, network, pake, protocol`
- **[magic-wormhole.rs](../drafts/brew/magic-wormhole.rs.md)**: Send a file between two computers by reading a short code aloud; the Rust take on Magic Wormhole, with direct connections through NATs and firewalls.  
  `file-transfer, network, pake, protocol, rust`
- **[mcpsnoop](../drafts/brew/mcpsnoop.md)**: A transparent proxy and terminal UI that shows every JSON-RPC message passing between an AI client and its MCP server, like Wireshark for MCP.  
  `debugging, json-rpc, mcp, protocol, proxy, tui`
- **[miniupnpc](../drafts/brew/miniupnpc.md)**: A tiny dependency-free C client that finds your router over UPnP and asks it to open ports, a hands-on door into how NAT traversal works.  
  `c, nat, network, protocol, ssdp, upnp`
- **[nak](../drafts/brew/nak.md)**: A single Go binary that lets you create, query, sign and relay Nostr events from the terminal, with JSON output you can pipe into jq.  
  `cli, go, json, network, nostr, protocol`
- **[NextTrace](../drafts/brew/nexttrace.md)**: A traceroute that labels every hop with its location and network owner, and can draw the route on a map.  
  `cli, icmp, network, routing, traceroute`
- **[ngrep](../drafts/brew/ngrep.md)**: ngrep is grep for the network: give it a regex and a filter, and it prints live packets whose payloads match.  
  `dns, http, network, packets, pcap, protocol`
- **[OATH Toolkit](../drafts/brew/oath-toolkit.md)**: Command-line tools for generating and checking the HOTP and TOTP one-time codes behind everyday two-factor logins, so you can compute them yourself.  
  `authentication, cli, hotp, otp, protocol, totp`
- **[pwnat](../drafts/brew/pwnat.md)**: A proxy that connects a client behind one NAT to a server behind another, with no port forwarding, no relay and no third party.  
  `icmp, nat, network, protocol, udp`
- **[rdap](../drafts/brew/rdap.md)**: A small Go client for RDAP, the JSON-over-HTTP successor to WHOIS, that finds the right registry server for a domain, IP or AS number on its own.  
  `dns, go, network, protocol, rdap, whois`
- **[runit](../drafts/brew/runit.md)**: A tiny init and service supervisor from the daemontools lineage, showing how Unix boots and keeps daemons alive with a few shell scripts.  
  `ancient, daemontools, init, supervision, unix`
- **[sipsak](../drafts/brew/sipsak.md)**: A command-line Swiss army knife for SIP, the signalling protocol behind VoIP calls, useful for poking at a SIP server from the terminal.  
  `network, protocol, sip, voip`
- **[slirp4netns](../drafts/brew/slirp4netns.md)**: Gives an unprivileged Linux network namespace a working internet connection with no root, using a TCP/IP stack that runs entirely in user space.  
  `containers, linux, namespaces, nat, network, rootless`
- **[ssh-audit](../drafts/brew/ssh-audit.md)**: Connects to an SSH server, or poses as one for your client, and lists every algorithm offered, each graded weak, legacy or fine.  
  `crypto, network, protocol, security, ssh`
- **[sshuttle](../drafts/brew/sshuttle.md)**: Tunnels whole subnets over a plain SSH connection, so you reach a remote network by its real addresses without a VPN or admin rights.  
  `network, proxy, ssh, tcp, vpn`
- **[ssldump](../drafts/brew/ssldump.md)**: A passive TLS analyzer that reads live traffic or a pcap and prints every handshake and record as text or JSON, with fingerprints included.  
  `fingerprinting, json, network, pcap, protocol, tls`
- **[stoken](../drafts/brew/stoken.md)**: An open-source reimplementation of the RSA SecurID software token that turns a seed into the six-digit login codes, from the command line.  
  `needs-token, protocol, securid, two-factor`
- **[streamripper](../drafts/brew/streamripper.md)**: A command-line recorder that captures an internet radio stream to disk and, per its description, cuts it into tracks using the titles the station sends.  
  `internet-radio, mp3, network, protocol, shoutcast`
- **[swaks](../drafts/brew/swaks.md)**: A command-line SMTP test tool that walks a mail server through a transaction step by step, printing every line of the conversation and stopping wherever you choose.  
  `email, perl, protocol, smtp, testing`
- **[tailcat](../drafts/brew/tailcat.md)**: A netcat that tunnels over Tailscale's WireGuard data plane with no account, no root and no setup, just a short address you hand to the other side.  
  `go, nat-traversal, netcat, network, tailscale, wireguard`
- **[tcpflow](../drafts/brew/tcpflow.md)**: tcpflow turns captured TCP traffic into a directory of files, one per connection and direction, so you can grep a network conversation like text.  
  `forensics, network, pcap, protocol, tcp`
- **[tcptraceroute](../drafts/brew/tcptraceroute.md)**: A traceroute that probes with TCP packets instead of ICMP or UDP, so you can see the path that ordinary connection attempts take.  
  `network, protocol, root, tcp, traceroute`
- **[Teamtype](../drafts/brew/teamtype.md)**: Teamtype lets two people edit the same local text files in real time, peer to peer, from whichever editor each prefers, with no server or account.  
  `collaboration, crdt, editors, local-first, peer-to-peer`
- **[tracebox](../drafts/brew/tracebox.md)**: A traceroute that reports what changed your packets on the way, revealing hidden middleboxes like NATs, firewalls and proxies rewriting headers.  
  `icmp, lua, middlebox, needs-root, network, protocol, traceroute`
- **[trzsz](../drafts/brew/trzsz.md)**: trz and tsz move files through your existing SSH terminal session, like rz/sz, but they work inside tmux, where the old tools do not.  
  `file-transfer, protocol, ssh, terminal, tmux`
- **[2ping](../drafts/brew/twoping.md)**: A ping that tells you whether a lost packet died on the way out or on the way back, using a three-way exchange with a listener.  
  `network, ping, protocol, python`
- **[ucspi-tcp](../drafts/brew/ucspi-tcp.md)**: D. J. Bernstein's tcpserver and tcpclient turn any program that reads stdin and writes stdout into a TCP server or client, no socket code needed.  
  `djb, inetd, network, tcp, unix`
- **[uni](../drafts/brew/uni.md)**: A command-line Unicode database: look up any character by name, codepoint, category or emoji keyword and see its bytes, entity and name.  
  `cli, emoji, text, unicode`
- **[websocketd](../drafts/brew/websocketd.md)**: Turns any program that reads stdin and writes stdout into a WebSocket server, so a ten-line shell script can talk to a browser.  
  `cgi, network, protocol, unix, websocket`
- **[whosthere](../drafts/brew/whosthere.md)**: A terminal UI that lists every device on your LAN by combining mDNS, SSDP and the ARP cache, with no root needed.  
  `arp, go, mdns, network, protocol, ssdp, tui`
- **[wormhole-william](../drafts/brew/wormhole-william.md)**: Send a file between two computers with a short spoken code instead of accounts or addresses, end-to-end encrypted, in a single Go binary.  
  `cryptography, file-transfer, go, network, protocol`
- **[zlint](../drafts/brew/zlint.md)**: A certificate linter that checks X.509 certificates against RFC 5280, CA/Browser Forum rules, and root store policies, the same checks CAs run before issuing.  
  `certificates, go, linter, pki, tls, x509`
- **[zsync](../drafts/brew/zsync.md)**: Downloads a new version of a file over plain HTTP by fetching only the parts that changed from your old copy, with rsync's algorithm run on the client.  
  `delta-transfer, http, network, protocol, rsync`

## afternoon

- **[ahcpd](../drafts/brew/ahcpd.md)**: A daemon that hands out IPv4, IPv6, DNS and NTP settings on mesh networks where DHCP and router discovery cannot reach every link.  
  `autoconfiguration, ipv6, mesh, network, protocol`
- **[amtterm](../drafts/brew/amtterm.md)**: A serial-over-LAN client for Intel AMT, the out-of-band management channel built into some business PCs, with terminal and GTK front ends.  
  `intel-amt, needs-hardware, network, protocol, serial`
- **[Argus](../drafts/brew/argus.md)**: A network flow sensor, in development since 1984, that turns live traffic or pcap files into compact flow records you can filter and summarise later.  
  `flow, forensics, monitoring, netflow, network, pcap`
- **[asn1c](../drafts/brew/asn1c.md)**: A compiler that turns ASN.1 schemas, the grammar behind X.509 certificates and phone network signalling, into C code that reads and writes BER, DER, PER and XER.  
  `asn1, c, compiler, protocol, serialization, x509`
- **[babeld](../drafts/brew/babeld.md)**: A small routing daemon for Babel, an IETF-standard protocol that lets wired and wireless mesh nodes find loop-free paths to each other.  
  `ipv6, mesh, network, protocol, routing`
- **[baresip](../drafts/brew/baresip.md)**: A small, modular SIP softphone in C that lets you watch a VoIP call get set up, negotiated and carried, all from a terminal.  
  `audio, network, protocol, sip, tui, voip`
- **[bgpdump](../drafts/brew/bgpdump.md)**: Decodes MRT and Zebra/Quagga dump files into readable BGP messages, a way to see how the internet's routes are actually recorded and exchanged.  
  `bgp, mrt, network, protocol, routing`
- **[BGPStream](../drafts/brew/bgpstream.md)**: Give it a time window and it streams real BGP routing updates from Route Views and RIPE RIS, one line per announcement or withdrawal.  
  `bgp, internet, network, protocol, routing`
- **[binkd](../drafts/brew/binkd.md)**: A mailer daemon that carries FidoNet mail and files over TCP/IP, a way to touch the store-and-forward BBS networks that predate the internet.  
  `ancient, bbs, fidonet, network, protocol`
- **[BitlBee](../drafts/brew/bitlbee.md)**: An IRC server that turns your instant-messaging accounts into IRC nicks and channels, so any IRC client can talk XMPP, Twitter and more.  
  `chat, gateway, irc, old-school, protocol, xmpp`
- **[Bombadillo](../drafts/brew/bombadillo.md)**: A terminal browser for the non-web internet: gopher, gemini and finger, in one client, for anyone curious what the net looked like before HTTP took over.  
  `finger, gemini, gopher, protocol, tui`
- **[cjdns](../drafts/brew/cjdns.md)**: An encrypted IPv6 mesh network where your address is derived from your public key, so no registry hands out addresses and no one can forge yours.  
  `cryptography, ipv6, mesh, network, protocol`
- **[daemontools](../drafts/brew/daemontools.md)**: D. J. Bernstein's minimal service supervisor: a directory with a run script is a service, and it gets restarted whenever it dies.  
  `logging, old-school, process-supervision, services, unix`
- **[D-Bus](../drafts/brew/dbus.md)**: The message bus that lets desktop programs on one machine talk to each other, with tools to watch and poke it from a shell.  
  `daemon, desktop, ipc, protocol`
- **[distcc](../drafts/brew/distcc.md)**: distcc spreads C and C++ compile jobs across machines on your network by shipping preprocessed source to volunteer servers and getting object files back.  
  `ancient, build, c, compiler, distributed, network, protocol`
- **[djbdns](../drafts/brew/djbdns.md)**: D. J. Bernstein's DNS suite: a caching resolver, authoritative servers and lookup tools, built as small separate programs with security as the stated concern.  
  `dns, network, old, protocol, unix`
- **[dns2tcp](../drafts/brew/dns2tcp.md)**: A client and server pair that wrap a TCP session inside DNS queries and replies, showing how a name lookup can carry arbitrary traffic.  
  `dns, network, protocol, tunnel`
- **[dnscrypt-proxy](../drafts/brew/dnscrypt-proxy.md)**: A local DNS proxy that wraps your machine's lookups in encrypted transports like DNSCrypt, DNS-over-HTTPS and Oblivious DoH, so you can see how resolver trust works.  
  `dns, encryption, network, privacy, protocol`
- **[dnsperf](../drafts/brew/dnsperf.md)**: A DNS load generator from DNS-OARC that replays a file of queries at a server and ramps the rate until a resolver stops keeping up.  
  `benchmarking, dns, network, protocol`
- **[DNSViz](../drafts/brew/dnsviz.md)**: Probes a domain's DNS and DNSSEC setup, then draws the chain of trust as a graph you can open, so you can see what resolvers check.  
  `dns, dnssec, graphviz, network, protocol, visual`
- **[Dragonbox](../drafts/brew/dragonbox.md)**: A C++ library that finds the shortest decimal string a float will read back as exactly, with a published proof of why it works.  
  `algorithms, c++, floating-point, library, math`
- **[Dynamips](../drafts/brew/dynamips.md)**: Dynamips emulates whole Cisco routers, so a real IOS image boots as a virtual router on your laptop and you can poke at routing from the inside.  
  `cisco, emulation, network, routing`
- **[EdgeVPN](../drafts/brew/edgevpn.md)**: A single Go binary that builds a private network between machines over libp2p, with no central server, just a shared token.  
  `go, libp2p, network, p2p, vpn`
- **[ejabberd](../drafts/brew/ejabberd.md)**: An Erlang server that speaks XMPP, MQTT and SIP from one config file, so you can run your own chat infrastructure and see how it works.  
  `chat, erlang, mqtt, protocol, server, xmpp`
- **[EPICS Base](../drafts/brew/epics-base.md)**: The control-system toolkit behind particle accelerators and telescopes, which runs as a soft IOC on your laptop so you can poke at it with no hardware.  
  `control-systems, network, physics, protocol`
- **[fedify](../drafts/brew/fedify.md)**: A command-line tool that fetches and prints raw ActivityPub objects, and gives you a throwaway public inbox to watch what a federated server sends.  
  `activitypub, debugging, fediverse, json-ld, network, protocol`
- **[fragroute](../drafts/brew/fragroute.md)**: A packet-mangling tool that rewrites your outgoing traffic to one host, fragmenting, reordering, and overlapping packets to show how intrusion detection systems get fooled.  
  `ids-evasion, ip-fragmentation, network, old, protocol`
- **[freeDiameter](../drafts/brew/freediameter.md)**: An open source C implementation of Diameter, the AAA protocol that succeeded RADIUS and quietly authenticates traffic inside telecom networks.  
  `aaa, diameter, network, protocol, telecom`
- **[fwknop](../drafts/brew/fwknop.md)**: Hides a service like SSH behind a default-drop firewall and opens it only when one encrypted, authenticated packet arrives, so nmap sees nothing listening.  
  `firewall, network, protocol, security, ssh`
- **[geph4](../drafts/brew/geph4.md)**: A command-line client for Geph, a censorship-circumvention tunnel that rotates bridge routes and opens local SOCKS5 and HTTP proxies.  
  `censorship, network, protocol, proxy, tunnel`
- **[git-annex](../drafts/brew/git-annex.md)**: git-annex lets git track huge files without storing their contents, and keeps a log of which drive holds which copy.  
  `cli, distributed, git, haskell, storage`
- **[git-cinnabar](../drafts/brew/git-cinnabar.md)**: A git remote helper that clones and pushes to Mercurial repositories, translating between the two object models without a local Mercurial clone underneath.  
  `git, mercurial, protocol, remote-helper, version-control`
- **[gnmic](../drafts/brew/gnmic.md)**: A command-line client for gNMI, the gRPC protocol modern network gear uses to expose config and live telemetry, which can also act as a telemetry collector.  
  `grpc, network, protocol, telemetry, yang`
- **[gocryptfs](../drafts/brew/gocryptfs.md)**: An encrypted overlay filesystem that shows a folder of encrypted files as plain ones, and makes file-by-file encryption easy to look inside.  
  `cryptography, encryption, filesystem, fuse, go`
- **[godap](../drafts/brew/godap.md)**: A terminal UI that lets you browse and edit an LDAP directory, mostly Active Directory, as an expandable tree of objects.  
  `active-directory, go, kerberos, ldap, protocol, tui`
- **[GPAC](../drafts/brew/gpac.md)**: A multimedia framework whose MP4Box tool opens up MP4 files and DASH streams, and whose gpac command lets you wire media filters together like a pipeline.  
  `containers, dash, filters, mp4, streaming, video`
- **[Hesiod](../drafts/brew/hesiod.md)**: A 1980s naming service that stores plain-text lookups as ordinary DNS TXT records, so any DNS server can double as a tiny directory.  
  `c-library, dns, historical, naming, protocol`
- **[hsd](../drafts/brew/hsd.md)**: A full node for Handshake, a blockchain that acts as a DNS root zone, with a built-in resolver you can query with dig.  
  `blockchain, dns, network, nodejs, protocol`
- **[I2P](../drafts/brew/i2p.md)**: A full anonymous network running inside the internet, with its own sites, mail, IRC and torrents, routed through volunteer peers.  
  `anonymity, java, network, overlay, protocol`
- **[i2pd](../drafts/brew/i2pd.md)**: A C++ router that joins I2P, an anonymous overlay network where websites and services live inside the network and hide their users' real IP addresses.  
  `anonymity, daemon, network, overlay-network, protocol`
- **[iodine](../drafts/brew/iodine.md)**: iodine carries IPv4 traffic inside DNS queries and replies, turning a protocol meant for looking up names into a point-to-point network link.  
  `dns, network, protocol, tun-tap, tunnel`
- **[ipmitool](../drafts/brew/ipmitool.md)**: A command-line client for the BMC, the tiny second computer inside most servers that can power-cycle the machine and read its sensors even when the OS is down.  
  `bmc, hardware, ipmi, network, protocol, servers`
- **[ipmiutil](../drafts/brew/ipmiutil.md)**: A suite of 23 command-line tools for talking to the hidden management controller inside server hardware: sensors, event logs, power, and a remote serial console.  
  `bmc, ipmi, protocol, server-management`
- **[ipv6toolkit](../drafts/brew/ipv6toolkit.md)**: Nineteen command-line tools that craft IPv6 packets by hand, so you can see how networks and devices react to Neighbor Discovery, fragments and extension headers.  
  `ipv6, network, packet-crafting, protocol, security`
- **[IRRToolSet](../drafts/brew/irrtoolset.md)**: Command-line tools for reading and analysing internet routing policies written in RPSL, the language networks use to publish who routes what in the Internet Routing Registries.  
  `bgp, network, protocol, routing, rpsl`
- **[jigdo](../drafts/brew/jigdo.md)**: Jigsaw Download rebuilds a huge CD or DVD image byte for byte from small pieces scattered across mirrors, using a text file you can edit.  
  `checksums, downloads, iso, network, protocol`
- **[knock](../drafts/brew/knock.md)**: A port-knocking server that sniffs raw packets for a secret sequence of port hits, then runs a command such as opening a firewall port.  
  `firewall, libpcap, network, protocol, security`
- **[launch_socket_server](../drafts/brew/launch_socket_server.md)**: A small macOS proxy that lets launchd bind a privileged port like 80 and hand connections to a server running as an ordinary user.  
  `go, launchd, macos, network, sockets`
- **[libcoap](../drafts/brew/libcoap.md)**: A reference C implementation of CoAP, the tiny HTTP-like protocol that sensors and IoT gear speak, with a client and server you can run locally.  
  `c, coap, iot, network, protocol, udp`
- **[liblouis](../drafts/brew/liblouis.md)**: A table-driven braille translator that turns text into braille and back again, the engine inside screen readers like NVDA and Orca.  
  `accessibility, braille, library, tables, text`
- **[libprotoident](../drafts/brew/libprotoident.md)**: A C library and three tools that name the application protocol of a network flow by looking at only the first four payload bytes in each direction.  
  `dpi, flows, network, pcap, protocol`
- **[librespot](../drafts/brew/librespot.md)**: An open-source Spotify Connect client in Rust that turns any computer into a headless speaker your Spotify app can see and play to.  
  `audio, library, network, protocol, rust, spotify`
- **[libusbmuxd](../drafts/brew/libusbmuxd.md)**: A client library and two tools, iproxy and inetcat, that tunnel TCP connections to an iPhone over USB, using the usbmux protocol Apple's own software uses.  
  `ios, needs-hardware, protocol, tunneling, usb`
- **[libusrsctp](../drafts/brew/libusrsctp.md)**: A C library that runs SCTP, the message-oriented TCP alternative with multi-streaming and multihoming, entirely in userland, with a discard server and client to watch it move data.  
  `c, library, network, protocol, sctp, transport`
- **[libwbxml](../drafts/brew/libwbxml.md)**: A C library and two converters for WBXML, the compact binary XML that WAP-era phones used for settings, sync and messages.  
  `binary-format, library, mobile, protocol, wap, wbxml, xml`
- **[lldpd](../drafts/brew/lldpd.md)**: A daemon that speaks LLDP, the neighbour-discovery protocol switches use constantly, so your machine can tell you which switch port it is plugged into.  
  `daemon, lldp, network, protocol`
- **[masscan](../drafts/brew/masscan.md)**: A TCP port scanner built to sweep huge address ranges, up to the whole IPv4 Internet, by randomly permuting probes with its own TCP/IP stack.  
  `c, network, port-scanner, protocol, security, tcp`
- **[Metaproxy](../drafts/brew/metaproxy.md)**: A router for Z39.50 and SRU library search protocols that fans one query out to many back-end databases and merges the results.  
  `libraries, network, protocol, proxy, sru, z39.50`
- **[minidlna (ReadyMedia)](../drafts/brew/minidlna.md)**: A small C daemon that serves your music, photos and video to TVs and media players on the home network, via DLNA/UPnP-AV.  
  `daemon, dlna, network, protocol, upnp`
- **[mkp224o](../drafts/brew/mkp224o.md)**: Brute-forces Tor v3 onion addresses until one starts with a prefix you choose, showing how a hidden service's name comes from its key.  
  `cryptography, ed25519, network, onion, tor`
- **[monocle](../drafts/brew/monocle.md)**: A Rust command-line tool for searching, parsing and live-watching BGP routing data, so you can see how the internet's routes change from a shell.  
  `bgp, internet, network, protocol, routing, rust`
- **[NaCl](../drafts/brew/nacl.md)**: A C crypto library by Daniel Bernstein and colleagues that fixes the algorithms for you, so you just say "sign this message" or "box this message".  
  `c, crypto, library, public-key, signatures`
- **[ncdc](../drafts/brew/ncdc.md)**: A terminal client for Direct Connect, the hub-based peer-to-peer file-sharing network, speaking both the ADC and NMDC protocols through an ncurses interface.  
  `file-sharing, network, p2p, protocol, tui`
- **[Net-SNMP](../drafts/brew/net-snmp.md)**: The reference toolkit for SNMP, the protocol routers, printers and UPSs use to report their state: query devices, receive traps, or run your own agent.  
  `monitoring, network, protocol, snmp`
- **[netatalk](../drafts/brew/netatalk.md)**: A free file server that speaks Apple's old AFP protocol, so anything from Classic Mac OS to modern macOS can mount shares from it.  
  `afp, apple, file-server, network, protocol, retro`
- **[netcode](../drafts/brew/netcode.md)**: A small C library that adds secure, token-authenticated connections on top of UDP, built for multiplayer games and a clear look at connection design.  
  `c, crypto, gamedev, library, network, protocol, udp`
- **[NORM](../drafts/brew/norm.md)**: A reliable multicast transport protocol from the US Naval Research Laboratory, where receivers ask for what they missed instead of acknowledging everything, with a C library and demo apps.  
  `c, library, multicast, network, protocol`
- **[ntopng](../drafts/brew/ntopng.md)**: A web-based traffic monitor that shows which hosts and application protocols are crossing your network, live, from a browser tab on port 3000.  
  `dpi, network, protocol, traffic-analysis, web-ui`
- **[obfs4proxy](../drafts/brew/obfs4proxy.md)**: A Tor pluggable transport that wraps Tor traffic in the obfs4 protocol, so censors have a harder time recognising it.  
  `censorship, network, protocol, proxy, tor`
- **[ocproxy](../drafts/brew/ocproxy.md)**: A userspace TCP/IP stack that turns an OpenConnect VPN tunnel into a local SOCKS5 server and forwarded ports, with no root and no routing changes.  
  `network, proxy, socks, tcp-ip, userspace, vpn`
- **[olsrd](../drafts/brew/olsrd.md)**: A routing daemon from community wireless mesh networks, where each node learns its neighbours and works out paths through the network with no central router.  
  `mesh, network, protocol, routing, wireless`
- **[OnionCat](../drafts/brew/onioncat.md)**: OnionCat turns a Tor hidden service or I2P identity into an IPv6 address on a TUN device, so ordinary IP tools can talk over the onion network.  
  `i2p, ipv6, network, overlay, tor, vpn`
- **[ooniprobe](../drafts/brew/ooniprobe.md)**: A command-line client that tests what your own internet connection blocks or interferes with, and contributes the results to a public censorship dataset running since 2012.  
  `censorship, measurement, network, open-data`
- **[open62541](../drafts/brew/open62541.md)**: A small C99 implementation of OPC UA, the industrial automation protocol most developers never see, as a library you can read and build a server from.  
  `c, industrial, library, network, protocol`
- **[OpenDHT](../drafts/brew/opendht.md)**: A C++17 distributed hash table you can join on the public network, with dhtnode, a command-line node for putting and getting values from strangers' machines.  
  `dht, library, network, p2p, protocol`
- **[Open Kermit](../drafts/brew/openkermit.md)**: C-Kermit, a serial and network communications package from 1981 with a built-in scripting language, file transfer protocol, and expect-style automation, still under active development.  
  `file-transfer, protocol, retro, scripting, serial, tui`
- **[opkssh](../drafts/brew/opkssh.md)**: Log in over SSH with an OpenID Connect identity like alice@gmail.com instead of long-lived keys, by hiding the identity token inside a standard SSH certificate.  
  `authentication, certificates, openid-connect, protocol, ssh`
- **[owamp](../drafts/brew/owamp.md)**: Measures network latency and packet loss in each direction separately between two hosts, instead of blending them into one round-trip number like ping.  
  `latency, measurement, network, protocol`
- **[p0f](../drafts/brew/p0f.md)**: p0f identifies the operating system and software on both ends of a network connection by listening only, sometimes from a single SYN packet, without sending a probe.  
  `fingerprinting, network, passive, protocol, tcp`
- **[pacparser](../drafts/brew/pacparser.md)**: A small library that runs proxy auto-config (PAC) JavaScript files outside a browser, so you can ask which proxy a given URL would get.  
  `javascript, library, network, pac, proxy`
- **[Pear](../drafts/brew/pear.md)**: A runtime for building and running apps that load directly from other peers, with no servers, using the Hypercore family of P2P modules.  
  `dht, hypercore, javascript, networking, p2p`
- **[ptunnel](../drafts/brew/ptunnel.md)**: Carries TCP connections inside ICMP echo packets, so an ssh session can ride on ordinary pings when a network blocks everything else.  
  `icmp, network, ping, protocol, tunnel`
- **[radvd](../drafts/brew/radvd.md)**: A small daemon that sends IPv6 Router Advertisements, the quiet messages that let every device on a LAN pick its own address and default router.  
  `daemon, ipv6, ndp, networking, protocol, slaac`
- **[rpki-client](../drafts/brew/rpki-client.md)**: An OpenBSD validator that fetches the global RPKI repositories and checks which networks may announce which internet routes, emitting data for routers.  
  `bgp, network, protocol, routing, security`
- **[rtp2httpd](../drafts/brew/rtp2httpd.md)**: A tiny C server that turns carrier multicast IPTV streams into plain HTTP, so any browser or player can watch what a set-top box would.  
  `iptv, multicast, network, protocol, rtp, rtsp`
- **[rtptools](../drafts/brew/rtptools.md)**: Six small Unix programs that record, replay, hand-build and relay RTP streams, the packet format underneath VoIP calls and video conferencing.  
  `network, packets, protocol, rtp, voip`
- **[s6](../drafts/brew/s6.md)**: A small toolbox of independent Unix programs for supervising services, descended from daemontools and runit, built to be assembled rather than used as one big init.  
  `daemontools, init, processes, supervision, unix`
- **[Samba](../drafts/brew/samba.md)**: Samba is the open source implementation of Windows file sharing (SMB) and Active Directory protocols, shipped with dozens of tools for poking at both.  
  `active-directory, cifs, file-sharing, network, protocol, smb`
- **[scamper](../drafts/brew/scamper.md)**: CAIDA's parallel traceroute and ping engine, built to probe thousands of Internet addresses at a set packet rate and map how the network connects.  
  `measurement, network, protocol, traceroute`
- **[sec](../drafts/brew/sec.md)**: Simple Event Correlator, a Perl daemon that watches event streams like logs and applies rules to spot patterns across them.  
  `daemon, events, logs, monitoring, perl`
- **[shairport-sync](../drafts/brew/shairport-sync.md)**: An AirPlay audio receiver that turns a Unix machine into a speaker target, and keeps playback locked to the sender's clock by resampling on the fly.  
  `airplay, audio, clock-sync, multi-room, network, protocol`
- **[SiLK](../drafts/brew/silk.md)**: A suite of about 70 piped command-line tools from CERT for querying huge archives of network flow records, the NetFlow-style telemetry most developers never see.  
  `ipfix, netflow, network, security`
- **[SIPp](../drafts/brew/sipp.md)**: A traffic generator for SIP, the signalling protocol behind VoIP calls, that plays scripted XML call flows against real phone systems.  
  `network, protocol, sip, testing, voip`
- **[sngrep](../drafts/brew/sngrep.md)**: A terminal viewer that draws SIP call message flows, so you can see how a VoIP call is set up and torn down.  
  `network, protocol, sip, tui, voip`
- **[Snort](../drafts/brew/snort.md)**: Snort reads network packets, checks them against written rules, and raises alerts, a hands-on way to see how intrusion detection actually works.  
  `ids, network, packets, pcap, rules`
- **[Snowflake](../drafts/brew/snowflake.md)**: A Tor pluggable transport that routes blocked users' traffic through volunteer WebRTC proxies, so it looks like an ordinary video call.  
  `censorship, go, network, protocol, tor, webrtc`
- **[libSRTP](../drafts/brew/srtp.md)**: Cisco's reference C library for SRTP, the encryption layer under WebRTC and VoIP calls, with a small demo that sends words over an encrypted stream.  
  `crypto, library, network, protocol, rtp, voip`
- **[ssh3](../drafts/brew/ssh3.md)**: An experimental remote shell that runs the SSH Connection Protocol over HTTP/3 and QUIC, so a server can hide behind a secret URL and answer 404 to scanners.  
  `go, http3, network, protocol, quic, ssh`
- **[sslh](../drafts/brew/sslh.md)**: A daemon that listens on one port, such as 443, sniffs each client's first packet, and routes SSH, HTTPS or VPN traffic to the right backend.  
  `network, protocol, proxy, ssh, tls`
- **[stone](../drafts/brew/stone.md)**: A tiny C program that relays TCP and UDP connections at the application layer, and can wrap plain services in SSL or tunnel streams through HTTP proxies.  
  `c, network, proxy, ssl, tcp, tunneling, udp`
- **[Stubby](../drafts/brew/stubby.md)**: A local DNS daemon that wraps your machine's plain DNS queries in TLS and sends them to a privacy resolver, with Wireshark ready to watch it.  
  `dns, network, privacy, protocol, tls`
- **[Stuntman](../drafts/brew/stuntman.md)**: A STUN server and client that tell you which public IP and port the internet sees you as, and probe how your NAT behaves.  
  `nat, network, protocol, stun, udp`
- **[switch-lan-play](../drafts/brew/switch-lan-play.md)**: Tunnels a Nintendo Switch's local-network traffic through a relay on the internet, so games that expect a LAN think distant friends are next door.  
  `arp, game, network, protocol, tunnel, udp`
- **[swtpm](../drafts/brew/swtpm.md)**: A software TPM emulator that gives virtual machines a trusted platform module with no hardware, and lets you see how TPM identity certificates get made.  
  `protocol, security, simulation, tpm, virtualization`
- **[tcpreplay](../drafts/brew/tcpreplay.md)**: A suite that takes a saved packet capture, optionally rewrites its headers, and sends the packets back onto a live network at the speed you pick.  
  `network, packets, pcap, protocol, testing`
- **[testssl.sh](../drafts/brew/testssl.md)**: A TLS scanner written in plain bash that probes a server's protocols, ciphers and known flaws one handshake at a time, on any port.  
  `bash, network, protocol, ssl, starttls, tls`
- **[Tile38](../drafts/brew/tile38.md)**: A geolocation database where adding the word FENCE to a spatial query turns it into a live stream of enter and exit events.  
  `database, geofence, geospatial, redis-protocol, server`
- **[tinc](../drafts/brew/tinc.md)**: A mesh VPN daemon where every node connects directly to every other, with no central hub and one config file per new node.  
  `mesh, network, protocol, tunnelling, vpn`
- **[TinySPARQL](../drafts/brew/tinysparql.md)**: A small RDF triple store you query with SPARQL 1.1, built as a GObject C library and the successor to GNOME's Tracker.  
  `gnome, library, rdf, semantic-web, sparql, triple-store`
- **[Toxiproxy](../drafts/brew/toxiproxy.md)**: A TCP proxy that lets you slow, drop, cut and reset connections to Redis, MySQL or anything else, on demand, from a CLI or an HTTP API.  
  `chaos-testing, go, latency, network, proxy, tcp`
- **[tsshd](../drafts/brew/tsshd.md)**: An SSH server that moves your session onto UDP after login, so it survives IP changes, sleep and dropped links, much like mosh.  
  `go, network, protocol, quic, roaming, ssh, udp`
- **[udp2raw-multiplatform](../drafts/brew/udp2raw-multiplatform.md)**: A tunnel that wraps UDP traffic in fake TCP or ICMP packets, so it slips past firewalls that block UDP, now built for Windows, Mac and BSD.  
  `firewall, network, protocol, raw-sockets, tunnel, udp`
- **[UFTP](../drafts/brew/uftp.md)**: Sends one encrypted file stream over UDP multicast to many receivers at once, repairing losses with selective retransmits. A door into one-to-many delivery.  
  `encryption, multicast, network, protocol, udp`
- **[vde](../drafts/brew/vde.md)**: A software Ethernet switch you can plug processes, VMs and ssh tunnels into, so you can build and rewire a virtual LAN from the shell.  
  `ethernet, network, simulation, switch, tunnels, virtualization`
- **[Veilid](../drafts/brew/veilid.md)**: An open-source peer-to-peer app framework where every running app is a node that relays end-to-end encrypted data, with no central server in the middle.  
  `network, p2p, privacy, protocol, rust`
- **[Wayland](../drafts/brew/wayland.md)**: The protocol that replaces X11 for talking to a display server, with wayland-scanner turning its XML protocol definitions into C code.  
  `compositor, display, protocol, x11`
- **[yaf](../drafts/brew/yaf.md)**: A flowmeter that reads packets from an interface or pcap file and writes compact IPFIX records, one per connection, with optional protocol details attached.  
  `ipfix, netflow, network, pcap, protocol`
- **[YAZ](../drafts/brew/yaz.md)**: A C toolkit and set of command-line tools for talking to Z39.50 and SRU servers, the old protocols behind library catalogue search.  
  `library, marc, network, protocol, sru, z39.50`
- **[ZMap](../drafts/brew/zmap.md)**: A stateless scanner that sends one packet per address and can sweep the whole public IPv4 space on a single port in under 45 minutes.  
  `ipv4, network, protocol, research, scanning`
- **[zvbi](../drafts/brew/zvbi.md)**: A C library that pulls Teletext and closed captions out of the vertical blanking interval of analog TV signals, the hidden data lines above the picture.  
  `analog-tv, broadcast, closed-captions, library, teletext, vbi`
- **[Zyre](../drafts/brew/zyre.md)**: A C library where programs on the same LAN find each other by UDP beacon and swap group messages with no broker, server, or configuration.  
  `discovery, library, network, p2p, protocol, zeromq`

## days-off

- **[GNUnet](../drafts/brew/gnunet.md)**: A protocol stack that tries to replace the Internet's plumbing with encrypted, metadata-hiding peer-to-peer networking, with about fifty command-line tools exposing its parts.  
  `naming, network, p2p, privacy, protocol`
- **[Heimdal](../drafts/brew/heimdal.md)**: A free Kerberos 5 implementation whose bundled tools let you look at tickets, keytabs and credential caches, the machinery behind single sign-on.  
  `authentication, gssapi, kerberos, network, pki, protocol`
