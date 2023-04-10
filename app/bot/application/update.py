from .utils import Message, CallbackQuery

class Update:

    def __init__(self, data):
        self.__dict__.update(data)
        self._effective_user = None

    @classmethod
    def de_json(cls, update, bot):
        data = {}
        data["message"] = Message.de_json(update.get("message"), bot)
        data["edited_message"] = Message.de_json(update.get("edited_message"), bot)
        data["callback_query"] = CallbackQuery.de_json(update.get("callback_query"))
        data["bot"] = bot
        return Update(data)

    @property
    def effective_user(self):
        """
        :class:`telegram.User`: The user that sent this update, no matter what kind of update this
        is. If no user is associated with this update, this gives :obj:`None`. This is the case
        if :attr:`channel_post`, :attr:`edited_channel_post` or :attr:`poll` is present.
        Example:
            * If :attr:`message` is present, this will give
              :attr:`telegram.Message.from_user`.
            * If :attr:`poll_answer` is present, this will give :attr:`telegram.PollAnswer.user`.
        """

        if self._effective_user:
            return self._effective_user

        user = None

        if self.message:
            user = self.message.from_user

        elif self.edited_message:
            user = self.edited_message.from_user

        elif self.callback_query:
            user = self.callback_query.from_user

        self._effective_user = user
        return user
