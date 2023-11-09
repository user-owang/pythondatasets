def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    lst1 = list(f'{num1}')
    lst2 = list(f'{num2}')

    freq1 = dict()
    freq2 = dict()

    for digit in set(lst1):
        freq1[digit] = lst1.count(digit)
    for digit in set(lst2):
        freq2[digit] = lst2.count(digit)
    
    return freq1 == freq2