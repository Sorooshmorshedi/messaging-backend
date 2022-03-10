from messaging.models import User, Message, Admin, Like, Archived, Channel, Group, Seen
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = User
        fields = '__all__'

class UserEditSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = User
        fields = 'username', 'first_name', 'last_name', 'phone', 'profile_picture', 'bio', 'id'


class MessageSerializer(serializers.ModelSerializer):
    replay_to = serializers.CharField(source='reply.sender.username', read_only=True)
    replay_text = serializers.CharField(source='reply.text', read_only=True)
    pic = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    file = serializers.FileField(max_length=None, use_url=True, allow_null=True, required=False)
    sender_name = serializers.CharField(source='sender.username', read_only=True)
    sender_pic = serializers.ImageField(source='sender.profile_picture', read_only=True)
    reciver_name = serializers.CharField(source='receiver.username', read_only=True)

    class Meta:
        model = Message
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    admin_pic = serializers.ImageField(source='user.profile_picture', read_only=True)
    name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Admin
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    pic = serializers.ImageField(source='user.profile_picture', read_only=True)
    name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Like
        fields = '__all__'


class SeenSerializer(serializers.ModelSerializer):
    seen_pic = serializers.ImageField(source='user.profile_picture', read_only=True)
    name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Seen
        fields = '__all__'


class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archived
        fields = '__all__'


class ChannelSerializer(serializers.ModelSerializer):
    creator_name = serializers.CharField(source='creator.username', read_only=True)

    class Meta:
        model = Channel
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    creator_name = serializers.CharField(source='creator.username', read_only=True)

    class Meta:
        model = Group
        fields = '__all__'


class GroupEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = 'id', 'pic', 'name', 'about', 'link', 'private'
