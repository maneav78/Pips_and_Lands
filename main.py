def encode_cd(n):
    if type(n) is int and 0 <= n <= 255:
        s = '00000000'
        s += bin(n)
        s = s[-1:len(s)-9:-1]
        main_s = 'P'
        p_or_l = ['P', 'L']
        num = 0
        for char in s:
            if char == 'b':
                main_s += p_or_l[0]*(8-num)
                break
            main_s += p_or_l[int(char)]
            if int(char):
                p_or_l = p_or_l[::-1]
            num += 1
        return main_s


    else:
        raise TypeError('The input must be integer in range [0,255]')


encode_cd(5)