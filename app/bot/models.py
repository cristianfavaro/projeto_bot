from django.db import models
from django.utils import timezone
from django.db.models import JSONField


# class ConversationContext(models.Model):
#     pass
# class UserContext(models.Model):
    
#     EMPRESASADICIONAR = 1
#     PALAVRASADICIONAR = 2
#     CONTEXT_CHOICES = (
#         (EMPRESASADICIONAR, 'Empresas Adicionar'),
#         (PALAVRASADICIONAR, 'Palavras Adicionar'),
#     )

#     user = models.OneToOneField("UserTelegram", related_name='context', on_delete=models.CASCADE)
#     updated = models.DateTimeField(auto_now=True)
#     context = models.IntegerField(choices=CONTEXT_CHOICES, null=True, blank=True) 

#     def __str__(self):
#         return "/" + self.get_context_display().replace(" ", "").lower()

class UserTelegram(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    chat_id = models.CharField(max_length=100, unique=True)
    photo_url = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return getattr(self, "first_name", "last_name") 

    class Meta:
        db_table = 'user_telegram'


    # #history
    # def create_history_context(self, text, reply_markup):
    #     from bot.models import HistoryContext
    #     HistoryContext.objects.create(
    #         user=self, 
    #         text = text,
    #         reply_markup = reply_markup,
    #     )
  
    # def clear_history_context(self):
    #     history = getattr(self, 'history', False)
    #     if history:
    #         self.history.all().delete()

    # def create_context(self, type):
    #     return UserContext.objects.update_or_create(
    #         user=self,
    #         defaults={"context": getattr(UserContext, type, UserContext.EMPRESASADICIONAR)},
    #     )   


class Message(models.Model):
    user = models.ForeignKey(UserTelegram, on_delete=models.CASCADE)
    created_dt = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return self.text 

    class Meta:
        db_table = 'message'

class ConversationContext(models.Model):
    # user = models.ForeignKey(UserTelegram, related_name='history', on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
