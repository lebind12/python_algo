def solve():
    R1, S = map(int, input().split(" "))

    # S = (R1 + R2) / 2
    # 2S - R1 = R2
    print(2 * S - R1)

if __name__ == "__main__":
    solve()