"""
    Name:  Ali Alwaily
    Date:  4 August 2026
    About: This program takes a string from the user and creates the Burrows-Wheeler
            Transform for the user.
    What is a Burrows-Wheeler Transform (BTW): It is a data transformation algorithm
            that uses string rotations of a string then "sorts all [of those] cyclic
            shifts of the [input string], and then reports the last character of
            each shift" (The Algorithm Design Manual pg 638). This procedure is also
            reversible.
    Example: Consider the example string DESIGN. First, append "$" to DESIGN, so you
            would get DESIGN$. Then, rotate that string six times (because DESIGN is
            six letters long). You get:
                    DESIGN$
                    $DESIGN
                    N$DESIG
                    GN$DESI
                    IGN$DES
                    SIGN$DE
                    ESIGN$D
            Now, sort these strings with the string that starts with $ to be the
            first element:
                    $DESIGN
                    DESIGN$
                    ESIGN$D
                    GN$DESI
                    IGN$DES
                    N$DESIG
                    SIGN$DE
            Finally, your BW Transform is all of the last characters of these seven
            strings, so N$DISGE is your transform!
    Uses of the BWT: The BWT is used frequently in DNA sequencing and database querying
            in general. BWT is also used in compression, like in bzip2.
            Dr. Skiena says: "The Burrows-Wheeler string is typically 10-15% more
            compressible than the original text, because repeated words turn into blocks
            of repeated characters" (638).

  **HOW TO USE THIS PYTHON PROGRAM: There is a two-step process:
            (a) First, create a new myBWT object, such as ``b1 = myBWT("HELLO")``
            (b) Then, call the BWTransform() function, see test cases below as an
                example.
"""

# BWT CLASS
class myBWT:
    # CONSTRUCTOR
    # Takes in a string and adds a "$" to the end.
    def __init__(self, string):
        self.BWString = string.upper() + "$"

    # GET THE BWString VARIABLE (helper function)
    def printString(self):
        return self.BWString

    # CREATE THE BURROWS-WHEELER MATRIX
    def BWMatrix(self):
        stringSize = len(self.BWString)
        mList = []                              # Create new empty list
        mList.append(self.BWString)
        for i in range(stringSize-1):
            toModify = mList[i]                 # Look at the ith element of the list
            endChar = toModify[-1:]             # Take the last character of toModify
            newString = toModify[:-1]           # Take the first n-1 characters of toModify
            newString = endChar + newString     # Concatenate them
            mList.append(newString)             # Append
        return mList

    # FIND BW TRANSFORM
    def BWTransform(self):
        mList = self.BWMatrix()                 # Create BW Matrix
        mList.sort()                            # Sort BW Matrix
        listSize = len(mList)                   # Get size of mList
        newChar = ""                            # Create empty string
        # For all strings, append the last character of each string to each other
        for i in range(listSize):
            newChar = newChar + mList[i][-1:]
        return newChar

# RECONSTRUCT BWT CLASS (WORK IN PROGRESS)
"""
def myBWTReconstruct:
    # CONSTRUCTOR
    # Takes in the BW Transform
    def __init__(self, string):
        self.BWTransform = string

    #
    #def ..
"""

# Testing
b1 = myBWT("HELLO")             # Creates new b1 object
print(b1.printString())         # Prints Initial String
b1Transform = b1.BWTransform()  # Creates and Outputs BW Transform
print(b1Transform)
print("--------------")

b2 = myBWT("BANANA")
print(b2.printString())
print(b2.BWTransform())
print("--------------")

b3 = myBWT("DESIGN")
print(b3.printString())
print(b3.BWTransform())
print("--------------")

