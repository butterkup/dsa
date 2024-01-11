# Testing data structures stored in ldsa package.

import pytest


# Test Heep data structure.
def test_heap_heapify_min():
    import heapq
    from ldsa import heap
    from random import randint

    heap.setheaptype(heap.HeapType.MIN)  # Set the global default Heap type
    for size in range(1, 100):
        array = tuple(randint(1, 1000) for _ in range(size))
        mheap, gheap = list(array), list(array)
        heap.heapify(mheap)
        heapq.heapify(gheap)  # generates min-heap by default
        assert mheap == gheap


def test_heap_heapify_max():
    import heapq
    from ldsa import heap
    from random import randint

    heap.setheaptype(heap.HeapType.MAX)  # Set the global default Heap type
    for _ in range(10):
        array = tuple(randint(1, 1000) for _ in range(100))
        mheap, gheap = list(array), list(array)
        heap.heapify(mheap)
        heapq._heapify_max(gheap)
        assert mheap == gheap


def test_heappush_min():
    import heapq
    from ldsa import heap
    from random import randint

    heap.setheaptype(heap.HeapType.MIN)  # Set the global default Heap type
    for _ in range(10):
        array = tuple(randint(1, 1000) for _ in range(100))
        mheap, gheap = list(array[:-1]), list(array[:-1])
        heap.heapify(mheap)
        heapq.heapify(gheap)  # generates a min-heap by default
        heap.heappush(mheap, array[-1])
        heapq.heappush(gheap, array[-1])
        assert mheap == gheap


def test_heappop_min():
    import heapq
    from ldsa import heap
    from random import randint

    heap.setheaptype(heap.HeapType.MIN)  # Set the global default Heap type
    for size in range(1, 100):
        array = tuple(randint(1, 5) for _ in range(size))
        mheap, gheap = list(array), list(array)
        heap.heapify(mheap)
        heapq.heapify(gheap)  # generates a min-heap by default
        heap.heappop(mheap)  # by default, removes the first element
        heapq.heappop(gheap)  # Simply removes the element at index 0
        assert mheap == gheap
    custom_test = (12, 16, 47, 30, 34, 50, 48, 43, 46, 38)  # Note: Min-Heap
    input_heap, target_index = list(custom_test), 1
    expected_output = [12, 30, 47, 38, 34, 50, 48, 43, 46]
    heap.heappop(input_heap, target_index)
    assert input_heap == expected_output


def _linked_list_seq_test(List):
    pylist, mylist = [], List()
    assert pylist == list(mylist)
    pylist = [1, 4, 2, 4, 3, 4, 5, 4]
    mylist = List(pylist)
    assert pylist == list(mylist)
    assert pylist.index(3) == mylist.index(3)
    assert pylist.count(4) == mylist.count(4)
    pylist.remove(4)
    mylist.remove(4)
    assert pylist == list(mylist)
    pylist[2] = 100
    mylist[2] = 100
    assert pylist == list(mylist)
    del pylist[3], mylist[3]
    assert pylist == list(mylist)
    assert mylist[-1] == pylist[-1]
    pylist.append(1000)
    mylist.append(1000)
    assert pylist == list(mylist)
    with pytest.raises(IndexError):
        mylist[len(mylist)]
    assert len(pylist) == len(mylist)
    for _ in range(pylist.count(4)):
        pylist.remove(4)
        mylist.remove(4)
    assert 4 not in mylist
    print(pylist, list(mylist))
    assert pylist == list(mylist)
    del mylist[-1], pylist[-1]
    del mylist[0], pylist[0]
    assert pylist == list(mylist)
    assert mylist and pylist
    temp = [10, 20]
    pylist += temp
    mylist += temp
    pylist.extend(temp)
    mylist.extend(temp)
    assert list(reversed(pylist)) == list(reversed(mylist))
    assert pylist.pop(3) == mylist.pop(3)
    value = 5000
    print(pylist, list(mylist))
    pylist.insert(3, value)
    mylist.insert(3, value)
    print(pylist, list(mylist))
    pylist.insert(0, value)
    mylist.insert(0, value)
    print(pylist, list(mylist))
    pylist.insert(-1, value)
    mylist.insert(-1, value)
    print(pylist, list(mylist))
    assert pylist == list(mylist)
    assert value in mylist


def test_singly_linked_list():
    from ldsa.linked_list.list import SinglyLinkedList

    _linked_list_seq_test(SinglyLinkedList)


def test_doubly_linked_list():
    from ldsa.linked_list.list import DoublyLinkedList

    _linked_list_seq_test(DoublyLinkedList)


def test_cirdoubly_linked_list():
    from ldsa.linked_list.list import CirDoublyLinkedList

    _linked_list_seq_test(CirDoublyLinkedList)


def test_deque():
    import ldsa.queue as queue

    q: queue.Deque[int] = queue.Deque(maxsize=7)

    with pytest.raises(queue.QueueEmpty):
        q.popleft()

    q.append(5)
    q.extend([1, 2, 3])
    q.extendleft([10, 20, 30])

    with pytest.raises(queue.QueueFull):
        q.appendleft(4)

    data = [30, 20, 10, 5, 1, 2, 3]
    for d in data:
        e = q.popleft()
        assert e == d


def test_queue():
    import ldsa.queue as queue

    q: queue.Queue[int] = queue.Queue(maxsize=3)

    with pytest.raises(queue.QueueEmpty):
        q.pop()

    q.extend([1, 2, 3])

    with pytest.raises(queue.QueueFull):
        q.append(4)

    data = [1, 2, 3]
    for d in data:
        e = q.pop()
        assert e == d


def test_lifo_queue():
    import random as rand, ldsa.queue as queue

    for _ in range(100):
        sample = rand.choices(range(1000), k=100)
        rand.shuffle(sample)
        stack = queue.LIFOQueue(sample)
        sample.reverse()
        for d in sample:
            p = stack.pop()
            assert d == p


def test_priority_queue():
    import random as rand, ldsa.queue as queue

    for _ in range(100):
        sample = rand.choices(range(1000), k=100)
        rand.shuffle(sample)
        data = sorted(sample)
        pqueue = queue.PriorityQueue(sample)
        for d in data:
            p = pqueue.pop()
            assert d == p
