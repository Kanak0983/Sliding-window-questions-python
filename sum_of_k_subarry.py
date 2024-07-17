def sum_of_k_subarray(arr,N,k):
    sum = 0

    for i in range(N):
        length = 0
        for j in range(i,N):
            length +=1
            if length ==k:
                maxi = float('-inf')
                mini = float('inf')

                for m in range (i, j+1):
                    maxi = max(maxi , arr[m])
                    mini = min(mini,arr[m])

                    sum += maxi + mini
    return sum
