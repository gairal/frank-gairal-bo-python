from rest_framework import serializers
from frank.rest_bo.models import Skill, Category, Education, Experience, Interest, Travel, Image

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'description', 'level')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('name', 'path')

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('name', 'description', 'display_order')

class CategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    interests = InterestSerializer(many=True)
    class Meta:
        model = Category
        fields = ('name', 'display_order', 'skills', 'interests')

class EducationSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    class Meta:
        model = Education
        fields = ('name', 'image', 'short_description', 'year_in', 'year_out', 'place', 'diploma', 'website', 'extra_info', 'description', 'skills')

class ExperienceSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    class Meta:
        model = Experience
        fields = ('name', 'image', 'description', 'date_in', 'date_out', 'place', 'website', 'title', 'accomplishments', 'display_order', 'skills')

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = ('place', 'latitude', 'longitude', 'display_order')