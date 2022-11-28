"""
Description: Class for cruiser object
<pre>
Name: Gabriel Krishnadasan, Alizea Hinz, Aidan Rooney, Marissa Nicole Esteban (Pascal)
Course: COMP-305 FA22
Professor: A. Nuzen
</pre>
"""

from ship import ship
class cruiser(ship):
    def __init__(self, name:str = "cruiser", length:int = 3, horizontal:bool = True) -> None:
        self.length = length
        self.horizontal = horizontal
        self.name = name

    def change_orientation(self):
        if self.horizontal == True:
            self.horizontal = False
        else:
            self.horizontal = True

    def set_orientation(self, orientation):
        self.horizontal = orientation
