from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'seed database for development.'

    def handle(self, *args, **options):
        run_seed()

    
def run_seed():
    print('seed')
    pass