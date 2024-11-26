from django.core.management.base import BaseCommand
from library_management_system.books.models import BookReservation
from django.utils.timezone import now

class Command(BaseCommand):
    help = 'Cancel expired book reservations'

    def handle(self, *args, **kwargs):
        expired_reservations = BookReservation.objects.filter(reserved_until__lt=now())
        for reservation in expired_reservations:
            reservation.book.stock_quantity += 1
            reservation.book.save()
            reservation.delete()
        self.stdout.write(self.style.SUCCESS("Expired reservations canceled."))
