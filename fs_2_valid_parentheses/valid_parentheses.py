def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if parens[len(parens)-1] == '(' or parens[0] == ')':
        return False
    if parens.count('(') != parens.count(')'):
        return False
    for index in range(1,len(parens)):
        if parens[0:index].count(')') > parens[0:index].count('('):
            return False
    return True