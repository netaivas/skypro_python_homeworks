class User:
    first_name = 'No name'
    last_name = 'unknown'

    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_first_name(self):
        print(self.first_name)
    
    def say_last_name(self):
        print(self.last_name)

    def say_full_name(self):
        print(self.first_name, self.last_name)
