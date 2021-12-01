spam = ['apples', 'bananas', 'tofu', 'cats']
def commaCode(your_list):
    if len(your_list) == 0:
        return(print("Must provide a list of non-zero length"))
    for i in range(len(your_list)) :
        if your_list[i] == your_list[0]:
            out_string = str(your_list[i]) + ", "
        elif your_list[i] == your_list[-1]:
            out_string += "and " + str(your_list[i])
        else:
            out_string += str(your_list[i]) + ", "
    return(out_string)
