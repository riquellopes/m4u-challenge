# encoding: utf-8
from __future__ import unicode_literals
import getpass
from django.core.management.base import BaseCommand

from mark.api import BookmarkUserApi


class Command(BaseCommand):
    help = "Create super user to bookmark admin."

    def add_arguments(self, parser):
        parser.add_argument('--username', dest="username", type=str)

    def handle(self, *args, **options):
        self.stdout.write("Antes de criar o super usuário, execute a task make dump.")
        try:
            if not options["username"]:
                options["username"] = raw_input("Username: ")

            password = getpass.getpass()

            api = BookmarkUserApi()
            api.create_super(options["username"], password)

            self.stdout.write("Super usuário criado com sucesso.")
        except:
            self.stdout.write("Erro ao criar super usuário")
