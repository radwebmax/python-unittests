import unittest
#import pytest
import xmlrunner

# class for Node with numbers
class Node:
    def __init__(self, num):
        self.num = num


# class for Priority queue
class PriorityQueue:

    def __init__(self):
        self.queue = list()

    def add(self, node):
        # if queue is empty
        if self.size() == 0:
            # add the new node
            self.queue.append(node)
        else:
            # traverse the queue to find the right place for new node
            for x in range(0, self.size()):
                insertNodeFirstDigit = int(str(node.num)[0])
                queueNodeFirstDigit = int(str(self.queue[x].num)[0])
                if insertNodeFirstDigit <= queueNodeFirstDigit:
                    if x == (self.size() - 1):
                        # add new node at the end
                        self.queue.insert(x + 1, node)
                    else:
                        continue
                else:
                    self.queue.insert(x, node)
                    return True

    def delete(self):
        # remove the first node from the queue
        firstElement = self.queue[0].num
        self.queue.pop(0)
        return firstElement


    #show and delete last element from queue
    def peek(self):
        lastElement = self.queue[self.size() - 1].num
        self.queue.pop(self.size()-1)
        return lastElement


    def show(self):
        for x in self.queue:
            print(str(x.num))


    def size(self):
        return len(self.queue)


pQueue = PriorityQueue()
"""
node1 = Node(2000)
node2 = Node(5211)
node3 = Node(913)
node4 = Node(2345)
node5 = Node(12)
node6 = Node(3333000)
node7 = Node(90)
pQueue.add(node1)
pQueue.add(node2)
pQueue.add(node3)
pQueue.add(node4)
pQueue.add(node5)
pQueue.add(node6)
pQueue.add(node7)
pQueue.delete()
pQueue.show()
print("\nLast element: ")
#print(pQueue.peek())
print("\n")
pQueue.show()
"""
class MyTest(unittest.TestCase):
    def test_peeking(self):
        node21 = Node(901)
        node22 = Node(64578)
        node23 = Node(70645878)
        mustBeLast = Node(1234)
        node25 = Node(567)
        pQueue.add(node21)
        pQueue.add(node22)
        pQueue.add(node23)
        pQueue.add(mustBeLast)
        pQueue.add(node25)
        self.assertEqual(mustBeLast.num, pQueue.peek())


    def test_deleting(self):
        mustBeFirst = Node(8)
        node22 = Node(54678)
        node23 = Node(62)
        node24 = Node(2365)
        node25 = Node(43265458)
        pQueue.add(mustBeFirst)
        pQueue.add(node22)
        pQueue.add(node23)
        pQueue.add(node24)
        pQueue.add(node25)
        self.assertEqual(mustBeFirst.num, pQueue.delete())


if __name__ == '__main__':
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)

#pytest.main()
