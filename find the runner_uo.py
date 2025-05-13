if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Convertimos a conjunto para eliminar duplicados y luego volvemos a lista
    unique_scores = list(set(arr))
    unique_scores.sort(reverse=True)  # ordenamos de mayor a menor

    print(unique_scores[1])  # el segundo valor más grande