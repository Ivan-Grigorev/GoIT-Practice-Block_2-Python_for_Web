class Foo:
    """Docstring for class Foo"""

    #: Doc comment 1
    #: bla bla
    bar = 1

    flox = 2.5  #: Doc comment flox

    baz = 2
    """Docstring for class attribute Foo.bar"""
    def __init__(self):
        #: Doc comment for constructor
        self.qux = 3

        self.spam = 4
        """Docstring for instance attribute spam"""
