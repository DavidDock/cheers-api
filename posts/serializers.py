from rest_framework import serializers
from posts.models import Post
from stars.models import Star
from cheers.models import Cheer


class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer
    Methods to get is_owner, star_id and like id and to validate image
    Returns own fields, profile_image profile_id, star_id and cheer_id
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    star_id = serializers.SerializerMethodField()
    cheer_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_star_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            star = Star.objects.filter(
                owner=user, post=obj
            ).first()
            return star.id if star else None
        return None

    def get_cheer_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            cheer = Cheer.objects.filter(
                owner=user, post=obj
            ).first()
            return cheer.id if cheer else None
        return None  

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'type', 'content', 'image', 'score',
            'star_id','cheer_id',
        ]