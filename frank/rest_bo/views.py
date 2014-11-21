from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from frank.rest_bo.models import Skill, Category, Education, Experience, Interest, Travel
from frank.rest_bo.serializers import UserSerializer, GroupSerializer, SkillSerializer, CategorySerializer, EducationSerializer, ExperienceSerializer, InterestSerializer, TravelSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
