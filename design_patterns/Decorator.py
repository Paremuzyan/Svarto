class Client:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Client name is: {self.name}\nage is: {self.age}'


class ClientDecorator(Client):

    def __init__(self, client):
        self.__client = client

    def getname(self):
        return self.__client.name

    def __str__(self):
        if self.__client.age >= 16:
            return f'The content is available for client {self.__client.name}'
        else:
            return f'The content is not available for client {self.__client.name}'


c = Client('Poghos', 17)
print(c)
print(ClientDecorator(c))