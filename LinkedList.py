class node:
    def __init__(self,value):
        self.__value = value
        self.__next = None
    
    def setNextNode(self,node):
        self.__next = node

    def getValue(self):
        return self.__value
    
    def getNextNode(self):
        return self.__next




class LinkedList:
    
    def __init__(self):
        self.__headNode = None
        self.__lastNode = None
        self.__listLength = 0

    def appendNode(self,value):
        new_node = node(value)
        if self.__headNode == None:
            self.__headNode = new_node
            self.__lastNode = new_node
        else:
            self.__lastNode.setNextNode(new_node)
            self.__lastNode = new_node
        self.__listLength +=1


    def addNode(self,node:node,index:int = None):
        if index == None:
            pre_node = self.__lastNode
            pre_node.setNextNode(node)
        else:
            pre_node = self.getNode(index-1)
            aft_node = self.getNode(index+1)
            pre_node.setNextNode(node)
            node.setNextNode(aft_node)
        self.__listLength +=1

    def arrayLinkList(self):
        if self.__headNode == None:
            return -1
        current_node = self.__headNode
        linklist_array = []
        while current_node != None:
            linklist_array.append(current_node.getValue())
            current_node = current_node.getNextNode()

        return linklist_array
    
    def __len__(self):
        return self.__listLength
    

    def getNode(self,index):
        if index > self.__listLength:
            return -1
        current_node = self.__headNode
        current_node_index = 0
        
        while current_node_index < index:
            current_node = current_node.getNextNode()
            current_node_index+=1

        return current_node
        

    
    def insertNode(self,value,index:int):
        if index > self.__listLength:
            return -1
        
        if self.__headNode == None:
            return -1
        
        new_node = node(value)
        current_node = self.getNode(index-1)
        
        
        pointer_node = current_node.getNextNode()
        current_node.setNextNode(new_node)
        new_node.setNextNode(pointer_node)
        
        self.__listLength +=1
    
    def findNodeValue(self,index:int):
        if index > self.__listLength:
            return -1
        
        if self.__headNode == None:
            return -1
        
        current_node = self.getNode(index)
        return current_node.getValue()
    
    def findNodeIndex(self,value):
        if self.__headNode == None:
            return -1
        current_node = self.__headNode
        current_node_value = current_node.getValue()
        current_node_index = 0
        while current_node != None :
            if  current_node_index >= self.__listLength-1:
                return -1
            if current_node_value == value:
                break
            current_node = current_node.getNextNode()
            current_node_value = current_node.getValue()
            current_node_index +=1
            
            

        return current_node_index
        
    def sorted(self):
        node_counter = 0
        current_node = self.__headNode
        while node_counter < self.__listLength-1:
            if current_node.getValue()>current_node.getNextNode().getValue():
                return False
            current_node = current_node.getNextNode()
            node_counter+=1
        return True

    
    def sort(self):
        if self.__headNode is None or self.__headNode.getNextNode() is None:
            return
        
        self.__headNode = self.__merge_sort(self.__headNode)

        # After sorting, update lastNode.
        current = self.__headNode
        while current.getNextNode() is not None:
            current = current.getNextNode()
        self.__lastNode = current


    def __merge_sort(self, head):
        if head is None or head.getNextNode() is None:
            return head
        
        middle = self.__get_middle(head)
        next_to_middle = middle.getNextNode()
        middle.setNextNode(None)

        left = self.__merge_sort(head)
        right = self.__merge_sort(next_to_middle)

        sorted_list = self.__sorted_merge(left, right)
        return sorted_list


    def __sorted_merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        
        if a.getValue() <= b.getValue():
            result = a
            result.setNextNode(self.__sorted_merge(a.getNextNode(), b))
        else:
            result = b
            result.setNextNode(self.__sorted_merge(a, b.getNextNode()))
        
        return result


    def __get_middle(self, head):
        if head is None:
            return head
        
        slow = head
        fast = head.getNextNode()

        while fast is not None:
            fast = fast.getNextNode()
            if fast is not None:
                slow = slow.getNextNode()
                fast = fast.getNextNode()

        return slow



    def remove(self,value):
        if self.__headNode == None:
            return -1
        
        current_node = self.__headNode
        current_node_value = current_node.getValue()
        node_counter = 0
        previous_node = None
        while current_node_value != value:
            node_counter += 1 
            if node_counter >= self.__listLength:
                return -1
            previous_node = current_node
            current_node = current_node.getNextNode()
            current_node_value = current_node.getValue()
        if previous_node == None:
            self.__headNode = current_node.getNextNode()
        else:
            previous_node.setNextNode(current_node.getNextNode())
        del current_node
        self.__listLength-=1


    def swap(self,index1:int,index2:int):
        if index1 > self.__listLength or index2 > self.__listLength or index1 > index2:
            return -1
        if self.getNode(index1) == self.__headNode and self.getNode(index2) == self.__lastNode:
            aft_headnode = self.__lastNode
            aft_lastnode = self.__headNode
            self.__headNode = aft_lastnode
            self.__lastNode = aft_headnode
        elif index2-index1 > 1:  
            node1 = self.getNode(index1)
            node1_pre = self.getNode(index1-1)
            node1_aft = self.getNode(index1+1)
            
            node2 = self.getNode(index2)
            node2_pre = self.getNode(index2-1)
            node2_aft = self.getNode(index2+1)
            if index1 == 0:
                self.__headNode = node2

            node1_pre.setNextNode(node2)
            node2.setNextNode(node1_aft)

            node2_pre.setNextNode(node1)
            node1.setNextNode(node2_aft)
        else:
            node1 = self.getNode(index1)
            node1_pre = self.getNode(index1-1)
            node2 = self.getNode(index2)
            node2_aft = self.getNode(index2+1)

            node1_pre.setNextNode(node2)
            node2.setNextNode(node1)
            node1.setNextNode(node2_aft)

    def rotate(self):
        top = self.__listLength-1
        bottom = 0
        while top >= bottom:
            

            self.swap(bottom,top)
            top -= 1
            bottom +=1
