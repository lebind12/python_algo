def solve():
    # A는 앨범에 수록된 곡의 개수
    # I는 평균 값
    # 평균 값은 저작권이 포함된 멜로디의 개수 / 앨범에 수록된 곡의 개수
    # I = math.ceil(X / A)
    # 이때 평균 값은 항상 올림한다. => I는 항상 올림 값
    # math.ceil(I) 이니까 X / A 가 I-1 초과부터 I까지
    A, I = map(int, input().split(" "))
    # I - 1 < X / A <= I
    # A * (I - 1) < X <= I * A
    print(A * (I - 1) + 1)

    

if __name__ == "__main__":
    solve()