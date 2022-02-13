from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=127)
    online = models.ManyToManyField(to=User, blank=True)

    def get_online_count(self) -> int:
        return self.online.count()

    def join(self, user) -> None:
        self.online.add(user)
        self.save()

    def leave(self, user) -> None:
        self.online.remove(user)
        self.save()

    def __str__(self) -> str:
        return f'{self.name} ({self.get_online_count()}'


class Message(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=511)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username}: {self.content} [{self.timestamp}]'
