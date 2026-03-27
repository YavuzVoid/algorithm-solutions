def extractAndAppendSponsoredNodes(head):
    if not head:
        return head
    even_head = head
    odd_head = head.next
    even = even_head
    odd = odd_head
    while even and even.next and even.next.next:
        even.next = even.next.next
        odd.next = odd.next.next if odd.next else None
        even = even.next
        odd = odd.next if odd else None
    even.next = None
    if odd:
        odd.next = None
    prev = None
    curr = even_head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    reversed_even = prev
    if not odd_head:
        return reversed_even
    temp = odd_head
    while temp.next:
        temp = temp.next
    temp.next = reversed_even
    return odd_head
