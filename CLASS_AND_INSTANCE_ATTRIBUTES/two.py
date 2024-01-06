#!/usr/bin/python3
# let us create a class attribute called Three_Laws
# it is a tuple with three laws
class Robot:
    Three_Laws = (
            """A robot may not injure a human being or, through inaction,
            allow a human being to come to harm.""",
            """A robot must obey the orders given to it by human beings,
            except where such orders would conflict with the First Law.""",
            """A robot must protect its own existence as long as such
            protection does not conflict with the First or Second Law."""
            )

    def __init__(self, name, year):
        self.name = name
        self.year = year
