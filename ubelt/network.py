import socket
import dns.resolver as dres
from whois import whois as whois_lookup
import click

def dns_lookup(url: str) -> None:
    try:
        ip = socket.gethostbyname(url)
        click.echo(ip)
    except Exception as e:
        click.echo(e)

def reverse_dns_lookup(ip: str) -> None:
    try:
        url = socket.gethostbyaddr(ip)[0]
        click.echo(url)
    except Exception as e:
        click.echo(e)

def whois_lookup(target: str) -> None:
    try:
        rsps = whois_lookup(target)
        click.echo(rsps)
    except Exception as e:
        click.echo(e)

def mx_lookup(url: str) -> None:
    try:
        mx = [x.exchange.to_text() for x in dres.Resolver().query(url, "MX")]
        click.echo(mx)
    except Exception as e:
        click.echo(e)

def ns_lookup(url: str) -> None:
    try:
        ns = [x.to_text() for x in dres.Resolver().query(url, "NS")]
        click.echo(ns)
    except Exception as e:
        click.echo(e)