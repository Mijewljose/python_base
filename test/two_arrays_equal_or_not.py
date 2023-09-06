class Solution:
    def check(self, A, B, N):
        freq_map = {}
        for i in range(N):
            if A[i] in freq_map:
                freq_map[A[i]] += 1
            else:
                freq_map[A[i]] = 1

        
        for i in range(N):
            if B[i] not in freq_map:
                return False
            freq_map[B[i]] -= 1

        
        for frequency in freq_map.values():
            if frequency != 0:
                return False
        return True


solution = Solution()

N = int(input("Enter the length of the arrays: "))


arr1 = []
print("Enter elements of the first array separated by spaces:")
arr1 = list(map(int, input().split()))


arr2 = []
print("Enter elements of the second array separated by spaces:")
arr2 = list(map(int, input().split()))
result = solution.check(arr1, arr2, N)
if result:
    print("The arrays are equal.")
else:
    print("The arrays are not equal.")
