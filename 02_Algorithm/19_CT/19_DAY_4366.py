'''
정식이의 은행업무
2진수와 3진수 각가의 수에서 한 자리만을 잘목 이걱하고 있음
'''
T = int(input())
for tc in range(1, T+1):
    sec = list(input())
    thr = list(input())


    for i in range(len(sec)):
        sec_lst = sec[:]
        if sec_lst[i] == '0':
            sec_lst[i] = '1'
        else:
            sec_lst[i] = '0'
        for j in range(len(thr)):
            thr_lst = thr[:]
            if thr_lst[j] == '0':
                thr_lst[j] = '1'

                thr_lst[j] = '2'

            elif thr_lst[j] == '1':
                thr_lst[j] = '1'

                thr_lst[j] = '2'
            else:
                thr_lst[j] = '0'

                thr_lst[j] = '1'

            if int(''.join(sec_lst), 2) == int(''.join(thr_lst), 3):
                print(f'#{tc} {int("".join(sec_lst), 2)}')
