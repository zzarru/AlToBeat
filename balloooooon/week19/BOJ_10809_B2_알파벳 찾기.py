import string

alph_list = list(string.ascii_lowercase)
dict_0={}
for i in alph_list:
    dict_0[i]=-1

abc=input()
for i in range(len(abc)):
    if abc[i] in dict_0:
        if dict_0[abc[i]] == -1:
            dict_0[abc[i]] = i
            
lst=dict_0.values()
print(*lst)