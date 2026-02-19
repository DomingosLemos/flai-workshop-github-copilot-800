from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Clearing existing data...")
        
        # Delete all existing data using Django ORM
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS("Existing data cleared."))
        
        # Create teams
        self.stdout.write("Creating teams...")
        team_marvel = Team.objects.create(
            name="Team Marvel",
            description="Earth's Mightiest Heroes",
            members_count=0
        )
        team_dc = Team.objects.create(
            name="Team DC",
            description="Justice League United",
            members_count=0
        )
        self.stdout.write(self.style.SUCCESS("Teams created."))
        
        # Create users (superheroes)
        self.stdout.write("Creating users...")
        marvel_heroes = [
            {"name": "Iron Man", "email": "tony.stark@avengers.com", "team": "Team Marvel"},
            {"name": "Captain America", "email": "steve.rogers@avengers.com", "team": "Team Marvel"},
            {"name": "Thor", "email": "thor.odinson@avengers.com", "team": "Team Marvel"},
            {"name": "Black Widow", "email": "natasha.romanoff@avengers.com", "team": "Team Marvel"},
            {"name": "Hulk", "email": "bruce.banner@avengers.com", "team": "Team Marvel"},
            {"name": "Spider-Man", "email": "peter.parker@avengers.com", "team": "Team Marvel"},
        ]
        
        dc_heroes = [
            {"name": "Superman", "email": "clark.kent@justiceleague.com", "team": "Team DC"},
            {"name": "Batman", "email": "bruce.wayne@justiceleague.com", "team": "Team DC"},
            {"name": "Wonder Woman", "email": "diana.prince@justiceleague.com", "team": "Team DC"},
            {"name": "Flash", "email": "barry.allen@justiceleague.com", "team": "Team DC"},
            {"name": "Aquaman", "email": "arthur.curry@justiceleague.com", "team": "Team DC"},
            {"name": "Green Lantern", "email": "hal.jordan@justiceleague.com", "team": "Team DC"},
        ]
        
        all_users = []
        for hero in marvel_heroes:
            user = User.objects.create(**hero)
            all_users.append(user)
        
        for hero in dc_heroes:
            user = User.objects.create(**hero)
            all_users.append(user)
        
        # Update team member counts
        team_marvel.members_count = len(marvel_heroes)
        team_marvel.save()
        team_dc.members_count = len(dc_heroes)
        team_dc.save()
        
        self.stdout.write(self.style.SUCCESS(f"Created {len(all_users)} users."))
        
        # Create workouts
        self.stdout.write("Creating workouts...")
        workouts_data = [
            {
                "name": "Super Strength Training",
                "description": "Build superhuman strength",
                "activity_type": "Strength Training",
                "difficulty": "Hard",
                "duration": 60,
                "calories_per_session": 500
            },
            {
                "name": "Speed Force Running",
                "description": "Run at supersonic speeds",
                "activity_type": "Running",
                "difficulty": "Medium",
                "duration": 45,
                "calories_per_session": 600
            },
            {
                "name": "Web-Slinging Cardio",
                "description": "Swing through the city",
                "activity_type": "Cardio",
                "difficulty": "Medium",
                "duration": 30,
                "calories_per_session": 400
            },
            {
                "name": "Asgardian Battle Workout",
                "description": "Train like a god",
                "activity_type": "Combat Training",
                "difficulty": "Hard",
                "duration": 90,
                "calories_per_session": 700
            },
            {
                "name": "Underwater Endurance",
                "description": "Build aquatic stamina",
                "activity_type": "Swimming",
                "difficulty": "Medium",
                "duration": 45,
                "calories_per_session": 450
            },
            {
                "name": "Detective Yoga",
                "description": "Mind and body balance",
                "activity_type": "Yoga",
                "difficulty": "Easy",
                "duration": 30,
                "calories_per_session": 200
            },
        ]
        
        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS(f"Created {len(workouts_data)} workouts."))
        
        # Create activities
        self.stdout.write("Creating activities...")
        activity_types = ["Running", "Cycling", "Swimming", "Yoga", "Strength Training", "Combat Training", "Cardio"]
        activities_created = 0
        
        for user in all_users:
            num_activities = random.randint(5, 15)
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)
                calories = random.randint(150, 800)
                date = datetime.now() - timedelta(days=random.randint(0, 30))
                
                Activity.objects.create(
                    user_email=user.email,
                    user_name=user.name,
                    activity_type=activity_type,
                    duration=duration,
                    calories=calories,
                    date=date,
                    team=user.team
                )
                activities_created += 1
        
        self.stdout.write(self.style.SUCCESS(f"Created {activities_created} activities."))
        
        # Create leaderboard entries
        self.stdout.write("Creating leaderboard entries...")
        leaderboard_entries = []
        
        for user in all_users:
            activities = Activity.objects.filter(user_email=user.email)
            total_activities = activities.count()
            total_calories = sum(activity.calories for activity in activities)
            total_duration = sum(activity.duration for activity in activities)
            
            entry = Leaderboard.objects.create(
                user_email=user.email,
                user_name=user.name,
                team=user.team,
                total_activities=total_activities,
                total_calories=total_calories,
                total_duration=total_duration,
                rank=0
            )
            leaderboard_entries.append(entry)
        
        # Update ranks based on total calories
        leaderboard_entries.sort(key=lambda x: x.total_calories, reverse=True)
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()
        
        self.stdout.write(self.style.SUCCESS(f"Created {len(leaderboard_entries)} leaderboard entries."))
        
        self.stdout.write(self.style.SUCCESS("\n=== Database Population Complete ==="))
        self.stdout.write(f"Teams: {Team.objects.count()}")
        self.stdout.write(f"Users: {User.objects.count()}")
        self.stdout.write(f"Activities: {Activity.objects.count()}")
        self.stdout.write(f"Workouts: {Workout.objects.count()}")
        self.stdout.write(f"Leaderboard Entries: {Leaderboard.objects.count()}")
