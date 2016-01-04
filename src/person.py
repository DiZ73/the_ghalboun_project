# Class that is the defining class for a Contact within the realm of a person's social network.
# @author davidkroell, ramzirizk
#
# This is the class which is instantiated into several references.

class Person:
    
    firstName = ""
    lastName  = ""
    DOB       = ""
    
    def __init__(self, v1, v2, v3):
        self.firstName = v1
        self.lastName  = v2
        self.DOB       = v3


    #Accessor Methods for the Person Class.
        
    def getFirstName():
        return self.firstName

    def getLastName():
        return self.lastName
    
    def getDOB():
        return self.DOB

    #Modifyer methods for the class

    def setFirstName(self, v):
        self.firstName = v

    def setLastName(self, v):
        self.lastName = v

    def setDOB(self, v):
        self.DOB = v

 # Test that the string is compiled.
    def toString(self):
        var = self.firstName + ' - ' + self.lastName + ' - ' + self.DOB
        return var
