team_name = 'Least Logic' # Only 10 chars displayed.
strategy_name = 'Very Logical'
strategy_description = 'How does this strategy decide: Logically'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'c'
    elif len(their_history)<4 and their_history[-1] == 'b':
        return 'c'
    elif len(their_history) >2:
        if their_history[-1] == 'c':
            return 'c'
    elif my_history[-2:] == 'bb':
        return 'c'
    elif len(their_history) >25:
            if their_history[-7] =='bbbbbbb':
                return 'b'
            if their_history[-11] == 'bbcbcbcbbbc':
                return 'b'
            elif my_history[-1] =='c':
                return 'c'
            elif my_history[-1] =='b':
                return 'b'
            else:
                return 'b'
    elif their_history[-2:] == 'bb':
        return 'b'
    elif their_history[-1] == 'b':
        return 'b'
    else:
        return 'c'

    return 'b'
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
    test_move(my_history='bbb',
              their_history='ccc',
              my_score=0, 
              their_score=0,
              result='b')             