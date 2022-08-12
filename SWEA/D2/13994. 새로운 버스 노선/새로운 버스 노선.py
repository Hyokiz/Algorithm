for tc in range(1, int(input())+1):
    no_sun = int(input())
    arr = [0] * 1001 # 빈 배열 생성
    for _ in range(no_sun):

        x, a, b = map(int, input().split())

        if x == 1: # 일반버스일때
            for i in range(a, b + 1):
                arr[i] += 1 # 모든 정류장을 한번씩

        elif x == 2: # 급행버스일때
            for i in range(a, b + 1, 2):
                arr[i] += 1 # a가 홀수이든, 짝수이든 간격을 2로 해주면 다 들어간다..

        else: # 광역 급행버스일 때
            for i in range(a, b + 1): 
                if a % 2 == 1 and (i % 3 == 0 and i % 10 != 0): # 홀수인 경우//()를 쳐줘야 한다.
                    arr[i] += 1

                elif a % 2 == 0 and i % 4 == 0: # 짝수인 경우
                    arr[i] += 1




    print('#{} {}'.format(tc, max(arr)))