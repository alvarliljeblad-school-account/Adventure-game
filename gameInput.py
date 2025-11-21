def get_str_input(possible_inputs:list,input_str:str = "->")->str:
    possible_inputs = map(lambda a: str(a), possible_inputs)
    """Returns an input if it is in list of possible inputs, else it will try again"""
    player_input = ""
    #Keep taking player input until a valid input is obtained
    while player_input not in possible_inputs:
        player_input = input(input_str)
    #Return that value
    return player_input