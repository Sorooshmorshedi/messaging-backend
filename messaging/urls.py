from django.urls import path, include
from django.views.generic import TemplateView
from messaging.views import UserApiView, UserDetail, MessageApiView, MessageDetail, SearchUser, AdminApiView, \
    AdminDetail, LikeApiView, LikeDetail, SeenApiView, ArchiveApiView, ChannelApiView, ChannelDetail, GroupDetail, \
    GroupApiView, Log, Sign, UserEdit, AccountChats, AccountGroups, AccountChannels, AccountPv, Unlike, GroupChats, \
    Groupmembers, ChannelChats, ChannelMembers, AddChannelMember, JoinChannel, Invielink, LeaveChannel, ChannelAdress, \
    AddGroupMember, LeaveGroup, JoinGroup, GInvielink, GroupEdit, ChannelAdmins, GroupAdmins, LoginView, LogOut, \
    ChannelSeen, GroupSeen, MessageSeen, AccountArchived, UnArchive, home, send_push

app_name = 'messaging'
urlpatterns = [
    path('user', UserApiView.as_view(), name='UserApi'),
    path('user/<int:pk>/', UserDetail.as_view(), name='UserDetail'),
    path('user/edit/<int:pk>/', UserEdit.as_view(), name='UserEdit'),
    path('search/<str:search>/', SearchUser.as_view(), name='SearchUserApi'),
    path('message', MessageApiView.as_view(), name='messageApi'),
    path('message/<int:pk>/', MessageDetail.as_view(), name='messageDetail'),
    path('admin', AdminApiView.as_view(), name='adminApi'),
    path('admin/<int:pk>/', AdminDetail.as_view(), name='adminDetail'),
    path('like', LikeApiView.as_view(), name='likeApi'),
    path('like/<int:pk>/', LikeDetail.as_view(), name='likeDetail'),
    path('seen', SeenApiView.as_view(), name='seenApi'),
    path('archive', ArchiveApiView.as_view(), name='ArchiveApi'),
    path('archive/<int:pk>/', AdminDetail.as_view(), name='AdminDetail'),
    path('channel', ChannelApiView.as_view(), name='channelApi'),
    path('channel/<int:pk>/', ChannelDetail.as_view(), name='channelDetail'),
    path('channel/admins/<int:pk>/', ChannelAdmins.as_view(), name='ChannelAdmins'),
    path('group/admins/<int:pk>/', GroupAdmins.as_view(), name='GroupAdmins'),
    path('group', GroupApiView.as_view(), name='GroupApi'),
    path('group/<int:pk>/', GroupDetail.as_view(), name='GroupDetail'),
    path('groupE/<int:pk>/', GroupEdit.as_view(), name='GroupEdit'),
    path('log', LoginView, name='login'),
    path('sign', Sign.as_view(), name='sign'),
    path('logout', LogOut, name='LogOut'),
    path('account/chats/<int:pk>/', AccountChats.as_view(), name='AccountChats'),
    path('account/archived/<int:pk>/', AccountArchived.as_view(), name='AccountArchived'),
    path('account/groups/<int:pk>/', AccountGroups.as_view(), name='AccountGroups'),
    path('account/channels/<int:pk>/', AccountChannels.as_view(), name='AccountChannels'),
    path('account/pv/<int:pk1>/<int:pk2>/', AccountPv.as_view(), name='AccountPv'),
    path('unlike/<int:pk1>/<int:pk2>/', Unlike.as_view(), name='unlike'),
    path('seen/channel/<int:pk1>/<int:pk2>/', ChannelSeen.as_view(), name='ChannelSeen'),
    path('seen/group/<int:pk1>/<int:pk2>/', GroupSeen.as_view(), name='GroupSeen'),
    path('group/chats/<int:pk1>', GroupChats.as_view(), name='GroupChats'),
    path('group/members/<int:pk1>', Groupmembers.as_view(), name='Groupmembers'),
    path('channel/chats/<int:pk1>', ChannelChats.as_view(), name='ChannelChats'),
    path('group/chats/<int:pk1>', GroupSeen.as_view(), name='GroupSeen'),
    path('message/seen/<int:pk1>', MessageSeen.as_view(), name='MessageSeen'),
    path('channel/members/<int:pk1>', ChannelMembers.as_view(), name='ChannelMembers'),
    path('channel/join/<int:pk1>/<int:pk2>/', JoinChannel.as_view(), name='JoinChannel'),
    path('group/join/<int:pk1>/<int:pk2>/', JoinGroup.as_view(), name='JoinGroup'),
    path('unarchive/<int:pk1>/<int:pk2>/', UnArchive.as_view(), name='UnArchive'),
    path('channel/leave/<int:pk1>/<int:pk2>/', LeaveChannel.as_view(), name='LeaveChannel'),
    path('channel/add/<int:pk>', AddChannelMember.as_view(), name='AddChannelMember'),
    path('group/add/<int:pk>', AddGroupMember.as_view(), name='AddGroupMember'),
    path('group/leave/<int:pk1>/<int:pk2>/', LeaveGroup.as_view(), name='LeaveGroup'),
    path('channel/link/<str:token>', Invielink.as_view(), name='Invielink'),
    path('group/link/<str:token>', GInvielink.as_view(), name='GInvielink'),
    path('c/<str:link>', ChannelAdress.as_view(), name='ChannelAdress'),
    path('h', home, name='home'),
    path('send_push', send_push),
    path('webpush/', include('webpush.urls')),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript')),

]

