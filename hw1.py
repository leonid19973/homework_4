dict={"a":1,"b":2,"c":3}
inverse_dic={}
def key_and_val():
    for key,val in dict.items():
        inverse_dic[val]=key
    print(inverse_dic)

key_and_val()


