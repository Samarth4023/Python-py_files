if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tp = tuple(integer_list)
    th = hash(tp)
    print(th)