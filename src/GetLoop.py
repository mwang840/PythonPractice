def loop_size(node):
    length = 1
    currentNode = getTheNode(node)
    currentNext = currentNode.next
    while(currentNode != currentNext):
        length = length + 1
        currentNext = currentNext.next
    return length

def getTheNode(node):
    first = node
    second = node.next
    while(first != second):
        first = first.next
        second = second.next.next
    return first

def main():
    
    pass