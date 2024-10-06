"""
for n circuluar sitting find winner if every kth person is eliminated
[1,2,3,4,5] k = 2
then after 1st iteration
[1,3,4,5] 2 was eliminated
[1,3,5]
[3,5]
[3] -> winner
"""
# Complexity O(n^2)
def winner(n,k):
    array = [i+1 for i in range(n)]
    print(array)

    def helper(array:list,start_index):
        if len(array) == 1:
            return array[0]
        
        index_to_remove = (start_index + k-1) % len(array)
        del array[index_to_remove]
        return helper(array,index_to_remove)
    return helper(array,0)

print(winner(5,2))

def josephus_winner_o_n(n,k):

    def josephus(n):
        if n == 1:
            return 0
        return (josephus(n-1) + k ) %n
    return josephus(n=n) + 1

print(josephus_winner_o_n(5,2))


def josephus_winner_o_n_iter(n,k):
    survivor = 0
    for i in range(2,n+1):
        survivor = (survivor + k)%i

    return survivor + 1

print(josephus_winner_o_n_iter(5,2))