#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str or text is None or len(text) < 0:
        raise TypeError('text must be a string')

    t = list(text)
    i = 0
    l = len(t)
    while i < l:
        if t[i] == '.' or t[i] == '?' or t[i] == ':':
            if i + 1 != len(t):
                if t[i + 1] == '.' or t[i + 1] == '?' or t[i + 1] == ':':
                    t.insert(i + 1, '\n\n')
                    l += 1
                elif t[i + 1] != ' ':
                    t.insert(i + 1, '\n\n')
                    l += 1
                else:
                    t[i + 1] = '\n\n'
            else:
                t.insert(i + 1, '\n\n')
                l += 1
        i += 1

    j = 0

    while j < l:
        if j + 1 != len(t):
            if t[j] == '\n\n' and t[j + 1] == ' ':
                t.pop(j + 1)
                l -= 1
                continue
        j += 1

    text2 = "".join(t)
    print(text2, end='')
