from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import CASCADE


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9]+$',
                message='نام کاربری باید از حدوف و اعداد انگلیسی تشکیل شود'
            )
        ],
        error_messages={
            'unique': ("this username already exists."),
        },
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.ImageField(default='', upload_to='store_image/', null=True, blank=True)
    bio = models.TextField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'

    def __str__(self):
        return self.name or self.username


class Group(models.Model):
    token = models.CharField(max_length=100, null=True, blank=True, unique=True)
    pic = models.ImageField(default='', upload_to='store_image/', null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=CASCADE, related_name="group")
    members = models.ManyToManyField(User, related_name="group_members")
    about = models.CharField(max_length=255, null=True, blank=True)
    private = models.BooleanField(default=False)
    link = models.CharField(max_length=50, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    @staticmethod
    def createtoken():
        from randstr import randstr
        return randstr(30)

    def save(self, *args, **kwargs):
        if not self.id:
            self.token = self.createtoken()
        super().save(*args, **kwargs)
        try:
            admin = Admin.objects.create(group=self, user=self.creator)
            admin.save()
        except:
            pass


class Channel(models.Model):
    token = models.CharField(max_length=100, null=True, blank=True, unique=True)
    private = models.BooleanField(default=False)
    pic = models.ImageField(default='', upload_to='store_image/', null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=CASCADE, related_name="channel")
    joined_users = models.ManyToManyField(User, related_name="channels")
    about = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=50, null=True, blank=True, unique=True)

    @staticmethod
    def createtoken():
        from randstr import randstr
        return randstr(30)

    def save(self, *args, **kwargs):
        if not self.id:
            self.token = self.createtoken()
        super().save(*args, **kwargs)
        try:
            admin = Admin.objects.create(channel=self, user=self.creator)
            admin.save()
        except:
            pass

    def __str__(self):
        return self.name


class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="admin")
    channel = models.ForeignKey(Channel, on_delete=CASCADE, related_name="admin", null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=CASCADE, related_name="admin", null=True, blank=True)

    def __str__(self):
        return "{} admin".format(self.user.username)

    def save(self, *args, **kwargs):
        if self.channel and not self.group:
            members = self.channel.joined_users.all()
            if self.user not in members:
                self.channel.joined_users.add(self.user)
                self.channel.save()
            if Admin.objects.filter(user=self.user, channel=self.channel):
                raise ValidationError('admin added once')
        if not self.channel and self.group:
            members = self.group.members.all()
            if self.user not in members:
                self.group.members.add(self.user)
                self.group.save()
            if Admin.objects.filter(user=self.user, group=self.group):
                raise ValidationError('admin added once')
        super().save(*args, **kwargs)


class Message(models.Model):
    text = models.CharField(max_length=500, null=True, blank=True)
    pic = models.ImageField(default='', upload_to='store_image/', null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=CASCADE, related_name="message")
    seened = models.BooleanField(default=False)
    receiver = models.ForeignKey(User, on_delete=CASCADE, related_name="receive_message", null=True, blank=True)
    channel = models.ForeignKey(Channel, on_delete=CASCADE, related_name="message", null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=CASCADE, related_name="message", null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name="replies", blank=True, null=True)

    def __str__(self):
        return self.sender.username

    def save(self, *args, **kwargs):
        if not self.id:
            import datetime
            self.date = datetime.datetime.now()
        super().save(*args, **kwargs)


class Like(models.Model):
    message = models.ForeignKey(Message, on_delete=CASCADE, related_name="like")
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="like")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} like {} message".format(self.user.username, self.message.sender.username)

    def save(self, *args, **kwargs):
        if Like.objects.filter(user=self.user, message=self.message):
            raise ValidationError('you like this once')
        super().save(*args, **kwargs)


class Seen(models.Model):
    message = models.ForeignKey(Message, on_delete=CASCADE, related_name="seen")
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="seen")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} seen {} message".format(self.user.username, self.message.sender.username)


class Archived(models.Model):
    message = models.ForeignKey(Message, on_delete=CASCADE, related_name="archive")
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="archive")

    def __str__(self):
        return "{} archived {} message".format(self.user.username, self.message.sender.username)

    def save(self, *args, **kwargs):
        if Archived.objects.filter(user=self.user, message=self.message):
            raise ValidationError('you archived this')
        super().save(*args, **kwargs)
