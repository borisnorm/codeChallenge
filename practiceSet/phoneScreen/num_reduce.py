#Given a list o numbers a1/b1, a2/b2, return sum in reduced form ab

#Sum it in fractional form, or keep decimals and try to reverse

#This is language specific question
#(0.25).asInteger_ratio()
#Simplify
#from Fractions import fraction
#Fraction(0.185).limit_denominator()A
#A fraction will be returned

from Fractions import fraction

class Solution:

    #Array of tuples ()
    def reduced_sum(array):
        #Fraction array is here
        deci_array = []
        for fraction in array:
            deci_array.append(fracion[0] / fraction[1])

        #Fraction array is here
        sum_value = reduce(lambda x: x + y, deci_array)
        return Fraction(sumValue).limit_denominator()


    #Find the amx difference in array such that larges appears after the smaller
    def max_diff(array):
        min_val = 1000000 #Max integer
        max_diff = 0
        for value in array:
            if value < min_val:
                min_val = value

            diff = value - min_val
            if diff > max_diff:
                max_diff = diff
        return diff

