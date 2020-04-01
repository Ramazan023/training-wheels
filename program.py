def func():
        height = 300
        width = 400
        for i in range(0, height):
            st = ''
            for j in range(0, width):
                if j > width / 2 - i and j < width / 2 + i:
                   st += '#'
                else:
                    st += '$'
            print(st)

if __name__ == '__main__':
    func()