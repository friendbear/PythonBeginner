class Person(object):
    def __init__(self, name):
        self.name = name

    def say(self):
        print(f'Hello {self.name}')


class ChatGPT(Person):
    def __init__(self, name='GPT3.5', auto_prompt=True, passwd='123'):
        super().__init__(name)
        self._auto_prompt = auto_prompt
        self.passwd = passwd

    @property
    def auto_prompt(self):
        return self._auto_prompt

    @auto_prompt.setter
    def auto_prompt(self, auto_prompt):
        if self.passwd == '456':
            self._auto_prompt = auto_prompt
        else:
            raise ValueError

    def say(self):
        if self.auto_prompt:
            print(f'Hello prompt {self.name}')
        else:
            print(f'Hello {self.name}')


if __name__ == '__main__':
    p = Person('Kuma')
    p.say()

    c = ChatGPT("GPT4", passwd='456')
    c.auto_prompt = False
    print(c.auto_prompt)
    c.say()
