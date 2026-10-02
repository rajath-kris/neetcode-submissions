# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head1 = l1
        head2 = l2
        l3 = ListNode()
        head3 = l3

        cur1 = head1
        cur2 = head2
        cur3 = head3
        prev = None
        print(cur3.val)
        carryover = 0

        i = 1
        while cur1 is not None or cur2 is not None:
            print(f"Running loop {i} time")
            i+= 1
            
            if cur1 is None:
                
                total_sum = cur2.val + carryover 
                print(f"L2 is bigger and sum is {total_sum}")
                carryover = 0
                cur2 = cur2.next

            elif cur2 is None:
                total_sum = cur1.val + carryover 
                print(f"L1 is bigger and sum is {total_sum}")
                carryover = 0
                cur1 = cur1.next


            else: 
                total_sum = cur1.val + cur2.val + carryover
                print(f"Both are fine, sum is {total_sum}")

                cur1 = cur1.next
                cur2 = cur2.next

            if total_sum < 10:
                print("Running lesser than 10 loop")
                node_val = total_sum
                carryover = 0
            else:
                node_val = total_sum - 10
                carryover = 1

            if prev is not None:
                prev.next = cur3

            cur3.val = node_val
            cur3.next = ListNode()
            prev = cur3
            cur3 = cur3.next

            
            print(f"The carryover is {carryover}")
            

        if carryover!= 0:
            cur3.val = carryover
            prev = cur3
    
        current = head3
        while current.next is not None:
            print(f"{current.val}")
            current = current.next

        prev.next = None
        return l3
            


            



        