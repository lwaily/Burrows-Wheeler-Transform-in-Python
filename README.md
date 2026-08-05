# Burrows-Wheeler-Transform-in-Python
This program takes a string from the user and creates the Burrows-Wheeler Transform for the user. (work in progress)

### ABOUT
What is a Burrows-Wheeler Transform (BTW): It is a data transformation algorithm that uses string rotations of a string then "sorts all [of those] cyclic shifts of the [input string], and then reports the last character of each shift" (The Algorithm Design Manual pg 638).
This procedure is also reversible.

### Example
Consider the example string DESIGN. First, append "$" to DESIGN, so you would get DESIGN$. Then, rotate that string six times (because DESIGN is six letters long). You get:
> DESIGN$
> $DESIGN
> N$DESIG
> GN$DESI
> IGN$DES
> SIGN$DE
> ESIGN$D
Now, sort these strings with the string that starts with $ to be the first element:
> $DESIGN
> DESIGN$
> ESIGN$D
> GN$DESI
> IGN$DES
> N$DESIG
> SIGN$DE
Finally, your BW Transform is all of the last characters of these seven strings, and N$DISGE is your transform!

### Uses of the BWT
The BWT is used frequently in DNA sequencing and database querying in general.
BWT is also used in compression, like in bzip2. Dr. Skiena says: "The Burrows-Wheeler string is typically 10-15% more compressible than the original text, because repeated words turn into blocks of repeated characters" (638).

### HOW TO USE THIS PYTHON PROGRAM: There is a two-step process:
1. First, create a new myBWT object, such as ``b1 = myBWT("HELLO")"
2. Then, call the BWTransform() function, see test cases below as an example.
