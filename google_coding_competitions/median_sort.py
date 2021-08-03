def main():
    data = input().split(' ')
    t = int(data[0])
    n = int(data[1])
    q = int(data[2])
    f = open('./log.log', 'w')
    f.write(f'{data}\n')
    while t > 0:
        R = [i for i in range(1, n + 1)]
        swap = True
        while swap and q > 0:
            swap = False
            for i in range(1, len(R) - 1):
                print(f'{R[i - 1]} {R[i]} {R[i + 1]}')
                q -= 1
                # f.write(f'{R[i - 1]} {R[i]} {R[i + 1]}\n')
                f.write(f'{R}\n')
                mid = int(input())
                if mid == R[i - 1]:
                    R[i - 1], R[i] = R[i], R[i - 1]
                    swap = True
                elif mid == R[i + 1]:
                    R[i], R[i + 1] = R[i + 1], R[i]
                    swap = True
        t -= 1
        print(' '.join(str(i) for i in R))

if __name__ == '__main__':
    main()
