from rest_framework import serializers
from test1.models import user_details, posts, review

class user_detailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user_details
        fields = '__all__'

class postsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = posts
        fields = '__all__'


class reviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = review
        fields = '__all__'
