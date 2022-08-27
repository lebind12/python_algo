def solve():
    gan = "0123456789"
    ji = "ABCDEFGHIJKL"

    # 2013년
    gan_start = 9
    ji_start = 5

    year = int(input())
    year = year - 2013
    # 왜 뒤로가는건 생각을 안했을까요?
    if year < 0:
        year = year + 60
    gan_start = (gan_start + year) % 10
    ji_start = (ji_start + year) % 12        
    print(ji[ji_start] + gan[gan_start])

if __name__ == "__main__":
    solve()