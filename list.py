if __name__ == '__main__':
    N = int(input())
    lista = []

    for _ in range(N):
        parts = input().split()
        cmd = parts[0]

        if cmd == "insert":
            lista.insert(int(parts[1]), int(parts[2]))
        elif cmd == "print":
            print(lista)
        elif cmd == "remove":
            lista.remove(int(parts[1]))
        elif cmd == "append":
            lista.append(int(parts[1]))
        elif cmd == "sort":
            lista.sort()
        elif cmd == "pop":
            lista.pop()
        elif cmd == "reverse":
            lista.reverse()
