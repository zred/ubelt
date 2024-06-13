from passlib.hash import sha512_crypt
from diceware import handle_options, get_passphrase
from re import findall
from random import choice, shuffle
from string import digits, punctuation
import click

def hash_password(password: str) -> None:
    try:
        click.echo(sha512_crypt.using(rounds=5000).hash(password))
    except Exception as e:
        click.echo(e)

def verify_hash(hash_to_verify: str, password: str) -> None:
    try:
        click.echo(sha512_crypt.verify(password, hash_to_verify))
    except Exception as e:
        click.echo(e)

def generate_passphrase(wc: int, dc: int, pc: int) -> None:
    p = findall('[A-Z][^A-Z]*', get_passphrase(handle_options(['-n', str(wc)]))) \
        + [choice(digits) for _ in range(dc)] \
        + [choice(punctuation) for _ in range(pc)]
    shuffle(p)
    click.echo(''.join(p))