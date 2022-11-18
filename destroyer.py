"""
Description: Class for destroyer object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

from ship import ship
class destroyer(ship):
    def __init__(self, length:int = 2, horizontal:bool = True) -> None:
        self.length = length
        self.horizontal = horizontal

    def change_orientation(self):
        if self.horizontal == True:
            self.horizontal = False
        else:
            self.horizontal = True