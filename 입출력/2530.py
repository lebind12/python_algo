def solve():
    """_summary_
    """
    start_hour, start_min, start_second = map(int, input().split(' '))
    second = int(input())

    start_second = start_second + second
    start_min = start_min + start_second // 60
    start_hour = start_hour + start_min // 60
    start_second = start_second % 60
    start_min = start_min % 60
    start_hour = start_hour % 24

    print(str(start_hour) + " " + str(start_min) + " " + str(start_second))

if __name__ == "__main__":
    solve()