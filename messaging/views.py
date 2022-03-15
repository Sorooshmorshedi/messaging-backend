from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from messaging.models import  User, Message, Admin, Like, Archived, Channel, Group, Seen
from messaging.serializers import UserSerializer, MessageSerializer, AdminSerializer, LikeSerializer, SeenSerializer, \
    ArchiveSerializer, ChannelSerializer, GroupSerializer, UserEditSerializer, GroupEditSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserApiView(APIView):
    def get(self, request):
        query = User.objects.all()
        serializer = UserSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserEdit(APIView):
    def put(self, request, pk):
        query = User.objects.filter(pk=pk).first()
        serializer = UserEditSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.filter(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        query = self.get_object(pk)
        serializer = UserSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SearchUser(APIView):
    def get_object(self, search):
        return User.objects.filter(Q(first_name__contains=search) | Q(last_name__contains=search))

    def get(self, request, search):
        query = self.get_object(search)
        serializers = UserSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


class MessageApiView(APIView):
    def get(self, request):
        query = Message.objects.all()
        serializer = MessageSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageDetail(APIView):
    def get_object(self, pk):
        try:
            return Message.objects.filter(pk=pk)
        except Message.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        query = self.get_object(pk)
        serializer = MessageSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = Message.objects.filter(pk=pk).first()
        serializer = MessageSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminApiView(APIView):
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminDetail(APIView):
    def get_object(self, pk):
        try:
            return Admin.objects.filter(pk=pk)
        except Admin.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        query = self.get_object(pk)
        serializer = AdminSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = Admin.objects.filter(pk=pk).first()
        serializer = AdminSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeApiView(APIView):
    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeDetail(APIView):
    def get_object(self, pk):
        try:
            return Like.objects.filter(pk=pk)
        except Like.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        query = Like.objects.filter(pk=pk).first()
        serializer = LikeSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Unlike(APIView):
    def get(self, request, pk1, pk2):
        account = User.objects.get(pk=pk1)
        message = Message.objects.get(pk=pk2)
        like = Like.objects.get(user=account, message=message)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class SeenApiView(APIView):
    def post(self, request):
        serializer = SeenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArchiveApiView(APIView):
    def post(self, request):
        serializer = ArchiveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArchiveDetail(APIView):
    def get_object(self, pk):
        try:
            return Archived.objects.filter(pk=pk)
        except Archived.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChannelApiView(APIView):
    def get(self, request):
        query = Channel.objects.all()
        serializer = ChannelSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ChannelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChannelDetail(APIView):
    def get_object(self, pk):
        try:
            return Channel.objects.filter(pk=pk)
        except Channel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        query = self.get_object(pk)
        serializer = ChannelSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = Channel.objects.filter(pk=pk).first()
        serializer = ChannelSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = Channel.objects.filter(pk=pk).first()
        admins = Admin.objects.filter(channel=query)
        admins.delete()
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupApiView(APIView):
    def get(self, request):
        query = Group.objects.all()
        serializer = GroupSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupEdit(APIView):
    def get_object(self, pk):
        try:
            return Group.objects.filter(pk=pk)
        except Group.DoesNotExist:
            raise Http404
    def put(self, request, pk):
        query = Group.objects.filter(pk=pk).first()
        serializer = GroupEditSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupDetail(APIView):
    def get_object(self, pk):
        try:
            return Group.objects.filter(pk=pk)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        query = self.get_object(pk)
        serializer = GroupSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = Group.objects.filter(pk=pk).first()
        serializer = GroupSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = Group.objects.filter(pk=pk).first()
        admins = Admin.objects.filter(group=query)
        admins.delete()
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AccountChats(APIView):
    def get(self, request, pk):
        account = User.objects.get(pk=pk)
        messages = Message.objects.filter(Q(sender=account)|Q(receiver=account))
        friends = []
        for message in messages:
            if message.sender not in friends:
                friends.append(message.sender)
            if message.receiver not in friends and message.receiver != None:
                friends.append(message.receiver)
        print(friends)
        serializer = UserSerializer(friends, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountArchived(APIView):
    def get(self, request, pk):
        account = User.objects.get(pk=pk)
        archives = Archived.objects.filter(user=account)
        messages = []
        for archive in archives:
            messages.append(archive.message)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountPv(APIView):
    def get(self, request, pk1, pk2):
        account = User.objects.get(pk=pk1)
        friend = User.objects.get(pk=pk2)
        messages = Message.objects.filter(Q(sender=account, receiver=friend)|Q(receiver=account, sender=friend)).order_by('date')
        friend_messages = Message.objects.filter(receiver=account, sender=friend)
        for message in friend_messages:
            message.seened = True
            message.save()
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class GroupChats(APIView):
    def get(self, request, pk1):
        group = Group.objects.get(pk=pk1)
        messages = Message.objects.filter(group=group).order_by('date')
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class Groupmembers(APIView):
    def get(self, request, pk1):
        group = Group.objects.get(pk=pk1)
        members = group.members.all()
        serializer = UserSerializer(members, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class MessageSeen(APIView):
    def get(self, request, pk1):
        message = Message.objects.get(pk=pk1)
        seen = Seen.objects.filter(message=message)
        serializer = SeenSerializer(seen, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class AccountGroups(APIView):
    def get(self, request, pk):
        account = User.objects.get(pk=pk)
        groups = Group.objects.filter(members=account)
        serializer = GroupSerializer(groups, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class ChannelChats(APIView):
    def get(self, request, pk1):
        channel = Channel.objects.get(pk=pk1)
        messages = Message.objects.filter(channel=channel).order_by('date')
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChannelSeen(APIView):
    def get(self, request, pk1, pk2):
        channel = Channel.objects.get(pk=pk1)
        user = User.objects.get(pk=pk2)
        messages = Message.objects.filter(channel=channel)
        for message in messages:
            if not Seen.objects.filter(message=message,user=user):
                seen = Seen.objects.create(message=message,user=user)
                seen.save()
        return Response({'ok': 1}, status=status.HTTP_200_OK)

class UnArchive(APIView):
    def get(self, request, pk1, pk2):
        message = Message.objects.get(pk=pk1)
        user = User.objects.get(pk=pk2)
        archive = Archived.objects.filter(user=user, message=message)
        archive.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GroupSeen(APIView):
    def get(self, request, pk1, pk2):
        group = Group.objects.get(pk=pk1)
        user = User.objects.get(pk=pk2)
        messages = Message.objects.filter(group=group)
        for message in messages:
            if not Seen.objects.filter(message=message,user=user):
                seen = Seen.objects.create(message=message,user=user)
                seen.save()
        return Response({'ok': 1}, status=status.HTTP_200_OK)

class ChannelMembers(APIView):
    def get(self, request, pk1):
        channel = Channel.objects.get(pk=pk1)
        members = channel.joined_users.all()
        serializer = UserSerializer(members, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class GroupAdmins(APIView):
    def get(self, request, pk):
        group = Group.objects.get(pk=pk)
        admins = Admin.objects.filter(group=group)
        serializer = AdminSerializer(admins, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChannelAdmins(APIView):
    def get(self, request, pk):
        channel = Channel.objects.get(pk=pk)
        admins = Admin.objects.filter(channel=channel)
        serializer = AdminSerializer(admins, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



class AccountChannels(APIView):
    def get(self, request, pk):
        account = User.objects.get(pk=pk)
        channels = Channel.objects.filter(joined_users=account)
        serializer = ChannelSerializer(channels, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddChannelMember(APIView):
    def post(self, request, pk):
        channel = Channel.objects.get(pk=pk)
        members = request.data['members']
        print(members)
        for member in members:
            user = User.objects.get(pk=member)
            if user not in channel.joined_users.all():
                channel.joined_users.add(user)
        return Response({'addmember': 'done'}, status=status.HTTP_200_OK)

class AddGroupMember(APIView):
    def post(self, request, pk):
        group = Group.objects.get(pk=pk)
        members = request.data['members']
        print(members)
        for member in members:
            user = User.objects.get(pk=member)
            if user not in group.members.all():
                group.members.add(user)
        return Response({'addmember': 'done'}, status=status.HTTP_200_OK)


class JoinChannel(APIView):
    def get(self, request, pk1, pk2):
        channel = Channel.objects.get(pk=pk1)
        user = User.objects.get(pk=pk2)
        channel.joined_users.add(user)
        return Response({'addmember': 'done'}, status=status.HTTP_200_OK)

class JoinGroup(APIView):
    def get(self, request, pk1, pk2):
        group = Group.objects.get(pk=pk1)
        user = User.objects.get(pk=pk2)
        group.members.add(user)
        return Response({'addmember': 'done'}, status=status.HTTP_200_OK)

class LeaveChannel(APIView):
    def get(self, request, pk1, pk2):
        channel = Channel.objects.get(pk=pk1)
        user = User.objects.get(pk=pk2)
        channel.joined_users.remove(user)
        return Response({'addmember': 'done'}, status=status.HTTP_200_OK)

class LeaveGroup(APIView):
    def get(self, request, pk1, pk2):
        group = Group.objects.get(pk=pk1)
        user = User.objects.get(pk=pk2)
        group.members.remove(user)
        return Response({'addmember': 'done'}, status=status.HTTP_200_OK)


class Invielink(APIView):
    def get(self, request, token):
        user = request.user
        if user.id:
            channel = Channel.objects.get(token=token)
            channel.joined_users.add(user)
            return redirect(
                'http://127.0.0.1:3000/message/channel/' + str(user.id)+ '/?id=' + str(channel.id))
        else:
            return redirect('http://127.0.0.1:3000')


class GInvielink(APIView):
    def get(self, request, token):
        user = request.user
        if user.id:
            group = Group.objects.get(token=token)
            group.members.add(user)
            return redirect(
                'http://127.0.0.1:3000/message/group/' + str(user.id)+ '/?id=' + str(group.id))
        else:
            return redirect('http://127.0.0.1:3000')


class ChannelAdress(APIView):
    def get(self, request, link):
        user = request.user
        if user.id:
            channel = Channel.objects.get(link=link)
            return redirect(
                'http://127.0.0.1:3000/message/channel/' + str(user.id)+ '/?id=' + str(channel.id))
        else:
            return redirect('http://127.0.0.1:3000')

@csrf_exempt
def LogoutView(request):
    if request.method == 'GET':
        logout(request)
        return redirect('http://127.0.0.1:3000')
    elif request.method == 'POST':
        logout(request)
        return redirect('http://127.0.0.1:3000')

class Log(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'id': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'id': 'not_found'}, status=status.HTTP_200_OK)

class Sign(APIView):
    def post(self, request):
        username = request.data['username']
        password1 = request.data['password']
        password2 = request.data['password1']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        phone = request.data['phone']
        if password1 == password2:
            user = User.objects.create(username=username,
                                       first_name=first_name, last_name= last_name, phone=phone)
            user.set_password(password1)
            user.save()
            login(request, user)
            return redirect('http://127.0.0.1:8000/api/log')

@csrf_exempt
def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('http://127.0.0.1:3000/message/' + str(user.id))
    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'messaging/base.html', {'form': form})



@csrf_exempt
def LogOut(request):
    if request.method == 'GET':
        logout(request)
        return redirect('http://127.0.0.1:8000/api/logout')
    elif request.method == 'POST':
        logout(request)
        return redirect('http://127.0.0.1:3000')


from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render, get_object_or_404
from webpush import send_user_notification
import json
from django.conf import settings


@require_GET
def home(request):
   webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
   vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
   user = request.user
   return render(request, 'messaging/home.html', {user: user, 'vapid_key': vapid_key})


@require_POST
@csrf_exempt
def send_push(request):
    try:
        head = request.POST['head']
        body = request.POST['body']
        user_id = request.POST['id']
        user = get_object_or_404(User, pk=user_id)
        payload = {'head': head, 'body': body}
        send_user_notification(user=user, payload=payload, ttl=1000)

        return JsonResponse(status=200, data={"message": "Web push successful"})
    except TypeError:
        return JsonResponse(status=500, data={"message": "An error occurred"})


