from django.test import TestCase

# Create your tests here.
# def sumOddLengthSubarrays(arr):
#         l=2
#         sum=0
#         for i in range(len(arr)-l):
#             for j in range(i,i+3):
#                 sum += arr[j]
#             print(sum)
#             l+=2
#         for i in range(len(arr)):
#             sum += arr[i]

# sumOddLengthSubarrays([1,2,3,4,5])


def sumOddLengthSubarrays( arr):
    ans, n = 0, len(arr)
    for i in range(n):
        j = i+1
        while j <= len(arr):
            ans += sum(arr[i:j])
            j+=2
    print(ans)

sumOddLengthSubarrays([1,2,3,4,5])