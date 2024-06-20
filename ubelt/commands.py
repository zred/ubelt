import click
from .network import dns_lookup, reverse_dns_lookup, lookup_whois, mx_lookup, ns_lookup
from .passwords import hash_password, verify_hash, generate_passphrase
from .file_server import serve_files, tail_file

@click.group()
def cli() -> None:
    pass

@click.command(help="Resolve URL to IP address")
@click.argument("url")
def dns(url: str) -> None:
    dns_lookup(url)

@click.command(help="Resolve IP address to URL")
@click.argument("ip")
def rdns(ip: str) -> None:
    reverse_dns_lookup(ip)

@click.command(help="Perform WHOIS lookup")
@click.argument("target")
def whois(target: str) -> None:
    lookup_whois(target)

@click.command(help="Perform MX lookup on URL")
@click.argument("url")
def mxlookup(url: str) -> None:
    mx_lookup(url)

@click.command(help="Perform NS lookup on URL")
@click.argument("url")
def nslookup(url: str) -> None:
    ns_lookup(url)

@click.command(help="Hash a password using sha512_crypt")
@click.password_option()
def hashpass(password: str) -> None:
    hash_password(password)

@click.command(help="Verify a sha512_crypt hash against a password prompt")
@click.argument("hash_to_verify")
@click.password_option()
def hashverify(hash_to_verify: str, password: str) -> None:
    verify_hash(hash_to_verify, password)

@click.command(help='Generate a strong passphrase')
@click.option('--wc', default=4, help='word count')
@click.option('--dc', default=2, help='digit count')
@click.option('--pc', default=2, help='punctuation count')
def passphrase(wc: int, dc: int, pc: int) -> None:
    generate_passphrase(wc, dc, pc)

@click.command(help="Print the last n lines of a file")
@click.option('-n', default=10, help="line count")
@click.argument("file")
def tail(file: str, n: int) -> None:
    tail_file(file, n)

@click.command()
@click.argument('path', default='.')
@click.option('--port', '-p', default=5000, help='Port to serve on')
def serve(path: str, port: int) -> None:
    serve_files(path, port)

cli.add_command(dns)
cli.add_command(rdns)
cli.add_command(whois)
cli.add_command(mxlookup)
cli.add_command(nslookup)
cli.add_command(hashpass)
cli.add_command(hashverify)
cli.add_command(passphrase)
cli.add_command(tail)
cli.add_command(serve)
