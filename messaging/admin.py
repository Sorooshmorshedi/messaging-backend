from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from messaging.models import User, Channel, Group, Message, Admin, Like, Seen, Archived

UserAdmin.fieldsets += (('profile pic', {'fields': ('profile_picture',)}),)
UserAdmin.fieldsets += (('biography', {'fields': ('bio',)}),)
UserAdmin.fieldsets += (('phone', {'fields': ('phone',)}),)

admin.site.register(User,UserAdmin)
admin.site.register(Group)
admin.site.register(Admin)
admin.site.register(Like)
admin.site.register(Archived)
admin.site.register(Message)
admin.site.register(Channel)
admin.site.register(Seen)
