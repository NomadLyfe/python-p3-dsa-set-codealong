class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)

    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary = {}
        return self.dictionary
    
    def __str__(self):
        string = ''
        for i, key in enumerate(self.dictionary.keys()):
            if i == len(self.dictionary.keys())-1:
                string += f'{key}'
            else:
                string += f'{key},'
        return f'MySet: {{{string}}}'