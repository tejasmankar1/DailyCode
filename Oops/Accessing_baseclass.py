class Chai:
    def __init__(self,type_,strength):
        self.type = self.type_
        self.strength = self.strength

############ Code duplication  ############

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        self.type = self.type_
        self.strength = self.strength
        self.spice_level = self.spice_level


############ Explicit method   ########

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        Chai.__init__(type_, strength)
        self.spice_level = self.spice_level

#############  super() method   ##############

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = self.spice_level
    