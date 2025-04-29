from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self):
        # Create test users
        user1 = User.objects.get_or_create(email='john.doe@example.com', defaults={'name': 'John Doe'})[0]
        user2 = User.objects.get_or_create(email='jane.smith@example.com', defaults={'name': 'Jane Smith'})[0]
        user3 = User.objects.get_or_create(email='alex.jones@example.com', defaults={'name': 'Alex Jones'})[0]
        user4 = User.objects.get_or_create(email='emma.watson@example.com', defaults={'name': 'Emma Watson'})[0]

        # Create test teams
        Team.objects.get_or_create(name='Team Alpha', defaults={'members': [user1.id, user2.id]})
        Team.objects.get_or_create(name='Team Beta', defaults={'members': [user3.id, user4.id]})

        # Create test activities
        Activity.objects.get_or_create(user=user1, type='Running', defaults={'duration': 30, 'date': '2025-04-28'})
        Activity.objects.get_or_create(user=user2, type='Cycling', defaults={'duration': 45, 'date': '2025-04-28'})
        Activity.objects.get_or_create(user=user3, type='Swimming', defaults={'duration': 60, 'date': '2025-04-28'})
        Activity.objects.get_or_create(user=user4, type='Yoga', defaults={'duration': 40, 'date': '2025-04-28'})

        # Create test leaderboard entries
        Leaderboard.objects.get_or_create(user=user1, defaults={'points': 100})
        Leaderboard.objects.get_or_create(user=user2, defaults={'points': 150})
        Leaderboard.objects.get_or_create(user=user3, defaults={'points': 200})
        Leaderboard.objects.get_or_create(user=user4, defaults={'points': 180})

        # Create test workouts
        Workout.objects.get_or_create(name='Pushups', defaults={'description': 'Do 20 pushups', 'duration': 10})
        Workout.objects.get_or_create(name='Squats', defaults={'description': 'Do 30 squats', 'duration': 15})
        Workout.objects.get_or_create(name='Plank', defaults={'description': 'Hold a plank for 2 minutes', 'duration': 2})
        Workout.objects.get_or_create(name='Lunges', defaults={'description': 'Do 20 lunges', 'duration': 15})

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
