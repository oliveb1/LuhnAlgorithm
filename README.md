# LuhnAlgorithm
Checks if a group of numbers will pass the Luhn Algorithm.

    

 ------------------------------------------
|Luhn Algorithm by Brian O., 07/15/19  |
 ------------------------------------------
The Luhn Algorithm is commonly used to verify credit card numbers, IMEI numbers, etc...
Luhn makes it possible to check numbers (credit card, SIRET, etc.) via a control key (called checksum, it is a number
of the number which makes it possible to check the others). If a character is incorrect, then Luhn's algorithm will
detect the error.
Starting with the right-most digit, double every other digit to the left of it. Then all of the undoubled and doubled
digits together. If the total is a multiple of 10, then the number passes the Luhn Algorithm.
For Luhn to be true:
    (double digits + undoubled digits) % 10 == 0
========================================================================================================================
