# 암호 출력
import sys
sys.stdin = open('input.txt', 'r')

pwd = {'001101': '0', '010011': '1', '111011': '2', '110001': '3', '100011': '4', 
        '110111': '5', '001011': '6', '111101': '7', '011001': '8', '101111': '9'}

T = int(input())
for tc in range(1, T+1):
    hex = input()
    cand = ''
    for h in hex:
        cand += bin(int(h, 16)).replace('0b', '').zfill(4)
    for i in range(len(cand)-1, -1, -1):
        if cand[i] == '1':
            idx = i
            break

    ans = []
    for i in range(idx//6):
        ans.append(pwd[cand[idx-6*i-5:idx-6*i+1]])
    ans.reverse()
    print(f'#{tc}', *ans)