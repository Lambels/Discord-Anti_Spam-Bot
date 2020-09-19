class User:
    '''Instance of the user, keeps track of his messages'''

    USER_LIST = []


    def __init__(self, name):
        self.name = name
        self.messages = []


    def check(self, message):
        '''The message argument is a discord, message object.'''
        for i in self.messages:
            if self.messages.count(i) >= 4:
                return i in str(message.content.lower())

    @classmethod
    def check_if_typed(cls, user):
        if len(cls.USER_LIST) == 0:
            return None
        try:
            for i in cls.USER_LIST:
                if i.name == user.author:
                    inst = i
        finally:
            return inst
