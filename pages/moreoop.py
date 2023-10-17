class OOP:
    __clsname__ = "OOP"
    __objcounter: int = 0
    _awep = 0

    def __new__(cls, *args, **kwargs):
        cls.__objcounter += 1
        return super().__new__(cls)

    def __init__(self):
        self._attribute: str = str()
        self._method: str = str()

    @classmethod
    def get_objs(cls):
        return cls.__objcounter

    @property
    def attribute(self):
        return self._attribute

    @property
    def method(self):
        return self._method

    @attribute.setter
    def attribute(self, attribute: str):
        self._attribute = attribute

    @attribute.getter
    def attribute(self):
        return self._attribute

    @method.setter
    def method(self, method: str):
        self._method = method

    @method.getter
    def method(self):
        return self._method


simpleoop = OOP()
simpleoop.method = "somemethod"
simpleoop.attribute = "someattribute"

print(simpleoop.attribute)
print(simpleoop.method)
print(OOP.get_objs())


class MOREOOP(OOP):
    pass


class EXTRAOOP(MOREOOP, OOP):
    pass
