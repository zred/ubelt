#!/bin/env python

import click
import socket
import os
import dns.resolver as dres
from whois import whois as whois_lookup
from passlib.hash import sha512_crypt
from diceware import handle_options, get_passphrase
from re import findall
from random import choice, shuffle
from string import digits, punctuation
from collections import deque
from flask import Flask, send_from_directory


@click.group()
def cli():
    pass


@click.command(help="Resolve URL to IP address")
@click.argument("url")
def dns(url):
    try:
        ip = socket.gethostbyname(url)
        click.echo(ip)
    except Exception as e:
        click.echo(e)


@click.command(help="Resolve IP address to URL")
@click.argument("ip")
def rdns(ip):
    try:
        url = socket.gethostbyaddr(ip)[0]
        click.echo(url)
    except Exception as e:
        click.echo(e)


@click.command(help="Perform WHOIS lookup")
@click.argument("target")
def whois(target):
    try:
        rsps = whois_lookup(target)
        click.echo(rsps)
    except Exception as e:
        click.echo(e)


@click.command(help="Perform MX lookup on URL")
@click.argument("url")
def mxlookup(url):
    try:
        mx = [x.exchange.to_text() for x in dres.Resolver().query(url, "MX")]
        click.echo(mx)
    except Exception as e:
        click.echo(e)


@click.command(help="Perform NS lookup on URL")
@click.argument("url")
def nslookup(url):
    try:
        ns = [x.to_text() for x in dres.Resolver().query(url, "NS")]
        click.echo(ns)
    except Exception as e:
        click.echo(e)


@click.command(help="Hash a password using sha512_crypt")
@click.password_option()
def hashpass(password):
    try:
        click.echo(sha512_crypt.using(rounds=5000).hash(password))
    except Exception as e:
        click.echo(e)


@click.command(
    help="Provide a sha512_crypt hash to be verified against a password prompt"
)
@click.argument("hash_to_verify")
@click.password_option()
def hashverify(hash_to_verify,password):
    try:
        click.echo(sha512_crypt.verify(password, hash_to_verify))
    except Exception as e:
        click.echo(e)


@click.command(help='Form a strong password')
@click.option('--wc',default=4,help='word count')
@click.option('--dc',default=2,help='digit count')
@click.option('--pc',default=2,help='punctuation count')
def passphrase(wc,dc,pc):
    p=findall('[A-Z][^A-Z]*', get_passphrase(handle_options(['-n',str(wc)]))) \
      + [choice(digits) for _ in range(dc)] \
      + [choice(punctuation) for _ in range(pc)]
    shuffle(p)
    click.echo(''.join(p))


@click.command(help="print the last n lines of file")
@click.option('-n',default=10,help="line count")
@click.argument("file")
def tail(file,n=10):
    with open(file) as f:
        for _ in deque(f,n):
            click.echo(_,nl=False)


app = Flask(__name__)

@app.route('/<path:path>')
def serve_file(path):
    """Serve a file from the specified PATH."""
    directory = os.getcwd()
    return send_from_directory(directory=directory, path=path)


@app.route('/')
def link_files():
    links = []
    files = [_ for _ in os.listdir('.') if not os.path.isdir(_)]
    for file in files:
        link = f'<a href="/{file}/">{file}</a>'
        links.append(link)
    return '<br>'.join(links)


@click.command()
@click.argument('path', default='.')
@click.option('--port', '-p', default=5000, help='Port to serve on')
def serve(path, port):
    """Serve files from PATH on PORT."""
    os.chdir(path)
    app.run(host='0.0.0.0', port=port)


cli.add_command(serve)
cli.add_command(tail)
cli.add_command(passphrase)
cli.add_command(hashverify)
cli.add_command(hashpass)
cli.add_command(mxlookup)
cli.add_command(nslookup)
cli.add_command(dns)
cli.add_command(rdns)
cli.add_command(whois)
if __name__ == "__main__":
    cli()
