from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1, created1 = User.objects.get_or_create(email='john.doe@example.com', defaults={'name': 'John Doe'})
        user2, created2 = User.objects.get_or_create(email='jane.smith@example.com', defaults={'name': 'Jane Smith'})

        # Create test teams
        team1, created_team = Team.objects.get_or_create(name='Team Alpha', defaults={'members': [user1.id, user2.id]})

        # Create test activities
        Activity.objects.get_or_create(user=user1, type='Running', defaults={'duration': 30, 'date': '2025-04-28'})
        Activity.objects.get_or_create(user=user2, type='Cycling', defaults={'duration': 45, 'date': '2025-04-28'})

        # Create test leaderboard entries
        Leaderboard.objects.get_or_create(user=user1, defaults={'points': 100})
        Leaderboard.objects.get_or_create(user=user2, defaults={'points': 150})

        # Create test workouts
        Workout.objects.get_or_create(name='Pushups', defaults={'description': 'Do 20 pushups', 'duration': 10})
        Workout.objects.get_or_create(name='Squats', defaults={'description': 'Do 30 squats', 'duration': 15})

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
