from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin configuration for User model"""
    list_display = ('name', 'email', 'team')
    list_filter = ('team',)
    search_fields = ('name', 'email', 'team')
    ordering = ('name',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin configuration for Team model"""
    list_display = ('name', 'members_count', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)
    list_per_page = 20


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin configuration for Activity model"""
    list_display = ('user_name', 'activity_type', 'duration', 'calories', 'date', 'team')
    list_filter = ('activity_type', 'team', 'date')
    search_fields = ('user_name', 'user_email', 'activity_type', 'team')
    ordering = ('-date',)
    date_hierarchy = 'date'
    list_per_page = 25


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin configuration for Leaderboard model"""
    list_display = ('rank', 'user_name', 'team', 'total_activities', 'total_calories', 'total_duration')
    list_filter = ('team',)
    search_fields = ('user_name', 'user_email', 'team')
    ordering = ('rank',)
    list_per_page = 20
    
    def get_readonly_fields(self, request, obj=None):
        """Make rank field readonly in the admin"""
        if obj:
            return ['rank']
        return []


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin configuration for Workout model"""
    list_display = ('name', 'activity_type', 'difficulty', 'duration', 'calories_per_session')
    list_filter = ('activity_type', 'difficulty')
    search_fields = ('name', 'description', 'activity_type')
    ordering = ('name',)
    list_per_page = 20


# Customize admin site header and title
admin.site.site_header = "OctoFit Tracker Administration"
admin.site.site_title = "OctoFit Admin Portal"
admin.site.index_title = "Welcome to OctoFit Tracker Admin"
