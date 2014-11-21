from django.contrib.auth.models import User, Group
from rest_framework import serializers
from frank.rest_bo.models import Skill, Category, Education, Experience, Interest, Travel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'description', 'level')

class CategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    class Meta:
        model = Category
        fields = ('name', 'display_order', 'skills')

class EducationSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    class Meta:
        model = Education
        fields = ('name', 'short_description', 'year_in', 'year_out', 'place', 'diploma', 'website', 'extra_info', 'description', 'skills')

class ExperienceSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    class Meta:
        model = Experience
        fields = ('name', 'description', 'date_in', 'date_out', 'place', 'website', 'title', 'accomplishments', 'display_order', 'skills')

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('name', 'description', 'display_order')

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = ('place', 'latitude', 'longitude', 'display_order')