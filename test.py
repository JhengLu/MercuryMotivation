if __name__ == '__main__':
    initial = 192 *1024
    current = int(192.001*1024)
    final = 384 * 1024
    firstStop = current
    second = final - current
    space = current - initial
    cmd = str(int(second)) + "M!" + str(int(firstStop)) +"M"

    print(cmd)
    print(current)
    print(initial)
    print(space)
