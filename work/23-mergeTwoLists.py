class Solution:
    def mergeKLists(self, lists):
        import heapq #调用堆
        minHeap = []
        for listi in lists:
            while listi:
                heapq.heappush(minHeap, listi.val) #把listi中的数据逐个加到堆中
                listi = listi.next
        dummy = ListNode(0) #构造虚节点
        p = dummy
        while minHeap:
            p.next = ListNode(heapq.heappop(minHeap)) #通过 heapq.heappop() 函数弹出堆中最小值
            p = p.next
        return dummy.next
