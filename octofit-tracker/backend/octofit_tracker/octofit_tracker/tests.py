from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import datetime
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    """Test cases for User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="testuser@example.com",
            team="Test Team"
        )
    
    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertEqual(self.user.team, "Test Team")
    
    def test_user_string_representation(self):
        """Test the string representation of a user"""
        self.assertEqual(str(self.user), "Test User")


class TeamModelTest(TestCase):
    """Test cases for Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team",
            members_count=5
        )
    
    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(self.team.description, "A test team")
        self.assertEqual(self.team.members_count, 5)
    
    def test_team_string_representation(self):
        """Test the string representation of a team"""
        self.assertEqual(str(self.team), "Test Team")


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email="testuser@example.com",
            user_name="Test User",
            activity_type="Running",
            duration=30,
            calories=300,
            date=datetime.now(),
            team="Test Team"
        )
    
    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.user_name, "Test User")
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)


class LeaderboardModelTest(TestCase):
    """Test cases for Leaderboard model"""
    
    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(
            user_email="testuser@example.com",
            user_name="Test User",
            team="Test Team",
            total_activities=10,
            total_calories=3000,
            total_duration=300,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        """Test that a leaderboard entry can be created"""
        self.assertEqual(self.leaderboard.user_name, "Test User")
        self.assertEqual(self.leaderboard.total_activities, 10)
        self.assertEqual(self.leaderboard.total_calories, 3000)
        self.assertEqual(self.leaderboard.rank, 1)


class WorkoutModelTest(TestCase):
    """Test cases for Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name="Morning Run",
            description="A refreshing morning run",
            activity_type="Running",
            difficulty="Medium",
            duration=30,
            calories_per_session=300
        )
    
    def test_workout_creation(self):
        """Test that a workout can be created"""
        self.assertEqual(self.workout.name, "Morning Run")
        self.assertEqual(self.workout.activity_type, "Running")
        self.assertEqual(self.workout.difficulty, "Medium")
        self.assertEqual(self.workout.duration, 30)


class UserAPITest(APITestCase):
    """Test cases for User API endpoints"""
    
    def setUp(self):
        self.user = User.objects.create(
            name="API Test User",
            email="apiuser@example.com",
            team="API Team"
        )
    
    def test_get_users_list(self):
        """Test that we can retrieve the users list"""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_user(self):
        """Test that we can create a new user"""
        data = {
            'name': 'New User',
            'email': 'newuser@example.com',
            'team': 'New Team'
        }
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamAPITest(APITestCase):
    """Test cases for Team API endpoints"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name="API Team",
            description="Team for API testing",
            members_count=3
        )
    
    def test_get_teams_list(self):
        """Test that we can retrieve the teams list"""
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_team(self):
        """Test that we can create a new team"""
        data = {
            'name': 'New Team',
            'description': 'A brand new team',
            'members_count': 0
        }
        response = self.client.post('/api/teams/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ActivityAPITest(APITestCase):
    """Test cases for Activity API endpoints"""
    
    def test_get_activities_list(self):
        """Test that we can retrieve the activities list"""
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_activity(self):
        """Test that we can create a new activity"""
        data = {
            'user_email': 'test@example.com',
            'user_name': 'Test User',
            'activity_type': 'Cycling',
            'duration': 45,
            'calories': 400,
            'date': datetime.now().isoformat(),
            'team': 'Test Team'
        }
        response = self.client.post('/api/activities/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LeaderboardAPITest(APITestCase):
    """Test cases for Leaderboard API endpoints"""
    
    def test_get_leaderboard_list(self):
        """Test that we can retrieve the leaderboard"""
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """Test cases for Workout API endpoints"""
    
    def test_get_workouts_list(self):
        """Test that we can retrieve the workouts list"""
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_workout(self):
        """Test that we can create a new workout"""
        data = {
            'name': 'Evening Yoga',
            'description': 'Relaxing yoga session',
            'activity_type': 'Yoga',
            'difficulty': 'Easy',
            'duration': 60,
            'calories_per_session': 200
        }
        response = self.client.post('/api/workouts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class APIRootTest(APITestCase):
    """Test cases for API root endpoint"""
    
    def test_api_root(self):
        """Test that the API root endpoint returns all available endpoints"""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
    
    def test_root_redirects_to_api(self):
        """Test that the root path points to API"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
