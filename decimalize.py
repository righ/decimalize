# coding: utf-8

CHARSET = '0123456789abcdefghijklmnopqrstuvwxyz'


class Decimalize(object):
    """decimal encode/decode manager
    """
    def __init__(self, charset=CHARSET):
        self.charset = charset
        self.len = len(charset)
        assert self.len == len(set(charset))

        self.map = {}
        for i, char in enumerate(charset):
            self.map[char] = i

    def encode(self, number):
        """
        10 -> n
        >>> hex = Decimalize('0123456789abcdef')
        >>> hex.encode(255)
        'ff'
        """
        string = ''
        while number:
            string = self.charset[number % self.len] + string
            number //= self.len
        return string

    def decode(self, string):
        """
        n -> 10
        >>> hex = Decimalize('0123456789abcdef')
        >>> hex.decode('ff')
        255
        """
        strlen = len(string) - 1
        number = 0
        for i, char in enumerate(string):
            number += self.map[char] * (self.len ** (strlen - i))
        return number


