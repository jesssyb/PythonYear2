class Rectangle:
    def __init__(self, width = 1, height = 1):
        self.width = width
        self.height = height

        def setWidth(self, width):
            self._width = width

        def setHeight(self, height):
            self._height = height

        def getWidth(self):
            return self._width

        def getHeight(self):
            return self._height
        def area(self):
            self._width * self._height
        def perimeter(self):
            return 2 * (self._width * self._height)
        def _str_(self):
            return "Width: ",self._width
        def __str__(self):
            return "Height: ",self._height
