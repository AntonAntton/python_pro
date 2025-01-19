class Person:
    """

    """
    def __new__(cls, *args, **kwargs):
        print('__new__')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print('__init__')
        self.name = name


    def __del__(self):
        print('__del__')

    def __delete__(self, instance):
        print('__delete__')


person = Person('Anton')
print(type(person))

print(type(Person))