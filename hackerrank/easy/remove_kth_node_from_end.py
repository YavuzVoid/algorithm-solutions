def removeKthNodeFromEnd(head, k):
    # k < 0 geçersiz
    if k < 0:
        return head

    dummy = SinglyLinkedListNode(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    # k 0-indexed olduğu için fast'i k+2 adım ileri götür
    # (dummy'den başlıyoruz, sondan 0 = son eleman)
    for i in range(k + 2):
        if fast is None:
            # k >= liste uzunluğu -> geçersiz
            return head
        fast = fast.next

    while fast is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next
