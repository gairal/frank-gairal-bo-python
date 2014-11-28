from rest_framework import filters
from rest_framework import viewsets

from frank.rest_bo.models import Skill, Category, Education, Experience, Interest, Travel, Image
from frank.rest_bo.serializers import SkillSerializer, CategorySerializer, EducationSerializer, ExperienceSerializer, InterestSerializer, TravelSerializer, ImageSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_fields = ('name', 'level')

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = ('name', 'display_order')
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('display_order', 'name')

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
