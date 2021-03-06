# from django.shortcuts import render
from sigi_op.views import CustomViewSet
from .serializers import CableStretchSerializer
from .serializers import CableStretchTypeSerializer
from .serializers import TubelooseSerializer
from .serializers import PostSerializer
from .models import CableStretch, CableStretchType
from .models import Tubeloose, Post


# Create your views here.
class CableStretchTypeListViewSet(CustomViewSet):
    class_name = CableStretchType
    order_param_name = 'description'
    queryset = CableStretchType.objects.all().order_by('description')
    serializer_class = CableStretchTypeSerializer


class CableStretchListViewSet(CustomViewSet):
    class_name = CableStretch
    order_param_name = 'fabricant'
    queryset = CableStretch.objects.all().order_by('fabricant')
    serializer_class = CableStretchSerializer


class TubelooseListViewSet(CustomViewSet):
    class_name = Tubeloose
    order_param_name = 'stretch_id'
    queryset = Tubeloose.objects.all().order_by('stretch_id')
    serializer_class = TubelooseSerializer


class PostListViewSet(CustomViewSet):
    class_name = Post
    order_param_name = 'cable_length'
    queryset = Post.objects.all().order_by('cable_length')
    serializer_class = PostSerializer
