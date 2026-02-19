from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team']
    
    def get_id(self, obj):
        return str(obj._id)

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'members_count']
    
    def get_id(self, obj):
        return str(obj._id)

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Activity
        fields = ['id', 'user_email', 'user_name', 'activity_type', 'duration', 'calories', 'date', 'team']
    
    def get_id(self, obj):
        return str(obj._id)

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_email', 'user_name', 'team', 'total_activities', 'total_calories', 'total_duration', 'rank']
    
    def get_id(self, obj):
        return str(obj._id)

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'activity_type', 'difficulty', 'duration', 'calories_per_session']
    
    def get_id(self, obj):
        return str(obj._id)
