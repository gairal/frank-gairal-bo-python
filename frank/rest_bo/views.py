from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets

from frank.rest_bo.models import Skill, Category, Education, Experience, Interest, Travel, Image
from frank.rest_bo.serializers import SkillSerializer, \
                                        CategorySerializer, \
                                        EducationSerializer, \
                                        ExperienceSerializer, \
                                        InterestSerializer, \
                                        TravelSerializer, \
                                        ImageSerializer, \
                                        SkillCategorySerializer, \
                                        InterestCategorySerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_fields = ('name', 'level')
    ordering_fields = ('name', 'level')

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class SkillCatViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.prefetch_related('skills').filter(skills__isnull=False).distinct('id')
    serializer_class = SkillCategorySerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_fields = ('name',)
    ordering_fields = ('display_order', 'name')

class InterestCatViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.prefetch_related('interests').filter(interests__isnull=False).distinct('id')
    serializer_class = InterestCategorySerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_fields = ('name',)
    ordering_fields = ('display_order', 'name')

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_fields = ('name',)
    ordering_fields = ('display_order', 'name')

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all().prefetch_related('image').prefetch_related('skills')
    serializer_class = EducationSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_fields = ('name', 'year_in', 'year_out')
    ordering_fields = ('display_order', 'name', 'year_in', 'year_out')

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all().prefetch_related('image').prefetch_related('skills')
    serializer_class = ExperienceSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_fields = ('name', 'date_in', 'date_out')
    ordering_fields = ('display_order', 'name', 'date_in', 'date_out')

class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_fields = ('name',)
    ordering_fields = ('display_order', 'name')

class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend)
    filter_fields = ('name',)
    ordering_fields = ('name', 'longitude', 'latitude')
