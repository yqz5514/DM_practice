#%%
def minTime(A, n, K):

     

    # Stores max element from A[]

    max_ability = A[0]
 

    # Find the maximum element

    for i in range(1, n):

        max_ability = max(max_ability, A[i])
 

    # Stores frequency of each element

    tmp = [0 for i in range(max_ability + 1)]
 

    # Stores minimum time required

    # to schedule all process

    count = 0
 

    # Count frequencies of elements

    for i in range(n):

        tmp[A[i]] += 1
 

    # Find the minimum time

    i = max_ability

     

    while(i >= 0):

        if (tmp[i] != 0):

            if (tmp[i] * i < K):

                 

                # Decrease the value

                # of K

                K -= (i * tmp[i])
 

                # Increment tmp[i/2]

                tmp[i // 2] += tmp[i]
 

                # Increment the count

                count += tmp[i]
 

                # Return count, if all

                # process are scheduled

                if (K <= 0):

                    return count

            else:

                 

                # Increment count

                if (K % i != 0):

                    count += (K // i) + 1

                else:

                    count += (K // i)
 

                # Return the count

                return count

        i -= 1
 

    # If it is not possible to

    # schedule all process

    return -1
 
# Driver code
#%%
if __name__ == '__main__':

     

    arr = [ 3, 1, 7, 2, 4 ]

    N = 5

    K = 15

     

    print(minTime(arr, N, K))
 
# %%
