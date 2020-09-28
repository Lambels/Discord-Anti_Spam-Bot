class User:
    '''Instance of the user, keeps track of his messages'''

    USER_LIST = []


    def __init__(self, name):
        self.name = name
        self.messages = []
        self.time = []


    def check(self, message):
        '''The message argument is a discord, message object.'''
        for i in self.messages:
            if self.messages.count(i) >= 4:
                return i in str(message.content.lower())


    def set_time(self, time):
        now = str(time)
        self.time.append((list(now)[17], list(now)[18]))


    def check_timer(self) -> bool:
        time_1 = int(self.time[0][0]) * 60 + int(self.time[0][1])
        time_2 = int(self.time[1][0]) * 60 + int(self.time[1][1])
        ans = time_2 - time_1
        if ans <= 3:
            return True
        else:
            return False


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
