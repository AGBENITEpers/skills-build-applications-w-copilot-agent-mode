from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email='john.doe@example.com', name='John Doe')
        user2 = User.objects.create(email='jane.smith@example.com', name='Jane Smith')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha', members=[user1.id, user2.id])

        # Create test activities
        Activity.objects.create(user=user1, type='Running', duration=30, date='2025-04-28')
        Activity.objects.create(user=user2, type='Cycling', duration=45, date='2025-04-28')

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, points=100)
        Leaderboard.objects.create(user=user2, points=150)

        # Create test workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', duration=10)
        Workout.objects.create(name='Squats', description='Do 30 squats', duration=15)

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
