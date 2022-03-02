def reverse_element(l):
    element=[]
    for i in l:
        element.append(i[::-1])
    return element

word=['abc','tuv','xyz']
print(reverse_element(word))