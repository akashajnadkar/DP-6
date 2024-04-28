'''
Time Complexity - O(n) for array method(DP). O(Nlogn) using brute force
Space Complexity - O(1) for DP method, O(logN) for brute force as we use a heap

Works on Leetcode
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        #Brute Force O(Nlogn)
        # hashSet = set()
        # primes = [2, 3, 5]
        # currUgly = 1
        # pq = []
        # count = 0
        # heapq.heappush(pq, currUgly)
        # hashSet.add(currUgly)
        # while count<n:
        #     currUgly = heapq.heappop(pq)
        #     count+=1
        #     for prime in primes:
        #         newUgly = currUgly*prime
        #         if newUgly not in hashSet:
        #             hashSet.add(newUgly)
        #             heapq.heappush(pq, newUgly)
        # return currUgly

        #pointers will point to current position
        p2,p3,p5 = 0, 0, 0
        #initial next ugly numbers are 2, 3, 5
        #n2, n3, n5 will store the product of 2, 3, 5 with number at p2, p3, p5 respectively
        n2, n3, n5 = 2, 3, 5
        arr = [0] * n
        arr[0] = 1
        for i in range(1,n):
            minNum = min(n2, n3, n5)
            arr[i] = minNum
            i+=1
            #increment p2 if n2 is minimum
            if minNum == n2:
                p2+=1
                n2 = 2*arr[p2]
            #increment p3 if n3 is minimum
            if minNum == n3:
                p3+=1
                n3 = 3*arr[p3]
            #increment p3 if n5 is minimum
            if minNum == n5:
                p5+=1
                n5 = 5*arr[p5]
        return arr[n-1]



        