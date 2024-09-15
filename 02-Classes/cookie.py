class Cookie:
    # CONSTRUCTOR OF A CLASS: def __init__, PARAMETER : color
    def __init__(self, color):
        self.color = color
        # self.color is the specific instance of the color we're creating

    # Methods that can be created other than the constructor: 
    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())
