---
name: opkssh
title: opkssh
source: brew
category: fundamentals
commitment: afternoon
tags: [afternoon, authentication, certificates, openid-connect, protocol, ssh]
homepage: https://eprint.iacr.org/2023/296
scout_score: 5
status: draft
---

# opkssh

**TLDR;** Log in over SSH with an OpenID Connect identity like alice@gmail.com instead of long-lived keys, by hiding the identity token inside a standard SSH certificate.

opkssh lets you sign in to servers with an identity from an OpenID Provider such as Google, Microsoft, GitLab or Keycloak. Running `opkssh login` opens a browser, you authenticate, and the tool writes an SSH key to ~/.ssh/id_ecdsa. That key carries a PK Token, an OpenID Connect ID Token bound to a public key. After that, plain `ssh` and `sftp` work as usual. The keys expire after 24 hours by default.

On the server, opkssh does not run a new daemon. It uses two existing SSH features. SSH certificates can carry arbitrary extensions, so the PK Token rides in one of them. sshd's AuthorizedKeysCommand then hands the certificate to `opkssh verify %u %k %t`, which checks the token against an allow-list of identities and Linux accounts.

The idea underneath is OpenPubkey, a research project that adds user public keys to OpenID Connect without breaking compatibility with existing providers. The identity provider does not need to know opkssh exists. The README puts the goal this way: SSH access managed "via identities like `alice@example.com` instead of long-lived SSH keys."

It is a good door into how SSH authentication actually works: certificates, extension fields, and the hook sshd offers for outside verifiers.

## Install

```
brew tap openpubkey/opkssh
brew install opkssh
# Client login needs a browser. Servers need root: the Linux installer script configures sshd and writes config under /etc/opk/. Other options: winget install openpubkey.opkssh, choco install opkssh -y, nix-shell -p opkssh.
```

## Try this

```
opkssh login
```
Opens a browser to sign in with your OpenID Provider, then writes an SSH key containing your PK Token to ~/.ssh/id_ecdsa.

```
opkssh inspect ~/.ssh/id_ecdsa.pub
```
Shows the details of the generated SSH key or certificate, including what it carries.

```
sudo opkssh add root alice@gmail.com google
```
On a configured server, adds a policy line allowing alice@gmail.com to log in as root through the Google issuer.

## What's unique

It does not change SSH's key format or add a daemon. It tucks the identity token into a standard certificate extension and lets sshd call a small verifier, so ssh and sftp stay unchanged.

## Caveats

The homepage is the OpenPubkey research paper, not a project site, and the code lives on GitHub; the shipped default client IDs are for testing only, and the Linux server install pipes a script into sudo bash.

## Links

- [OpenPubkey paper (homepage as given)](https://eprint.iacr.org/2023/296)
- [opkssh GitHub repository and README](https://github.com/openpubkey/opkssh)
- [opkssh CLI reference](https://github.com/openpubkey/opkssh/blob/main/docs/cli/opkssh.md)
- [OpenPubkey library](https://github.com/openpubkey/openpubkey)
