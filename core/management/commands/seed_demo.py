"""Create demo degrees, courses, one user per role and sample requests."""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seed the database with demo users (student, secretary, lecturer, head of department, admin) and sample requests."

    def handle(self, *args, **options):
        import populate

        populate.main()
