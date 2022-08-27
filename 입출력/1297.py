
def solve():
    D, H, W = map(int, input().split(" "))
    # 대각선 길이 == sqrt(H^2 + W^2)
    # 근데 H, W는 비율이니까 9 16이라고 하면 하나로 통일 가능
    # H : W = 9 : 16 => 9W = 16H => W = 16H / 9
    # D^2 = H^2 + (16H / 9)^2

    D = D*D
    

if __name__ == "__main__":
    solve()