class Link(object):
    def __init__(self, key, datum, next=None, previous=None):
        self.__key=key
        self.__data=datum
        self.__next=next
        self.__previous=previous
    
    def getKey(self): return self.__key
    def getData(self): return self.__data
    def setData(self, datum): self.__data=datum
    
    def getNext(self): return self.__next
    def setNext(self,link): self.__next=link
    
    def getPrevious(self): return self.__previous
    def setPrevious(self,link): self.__previous=link
    
    def isLast(self): return self.__next is None
    def isFirst(self): return self.__previous is None
    def __str__(self): return str((self.getKey(),self.getData()))
    
class DLL(object):
    def __init__(self): self.__first=self.__last=None
    def __str__(self): 
        ans="["
        link=self.__first
        while link is not None:
            if len(ans)>1:
                ans+="==>"
            ans+=str(link)
            link=link.getNext()
        ans+="]"
        return ans
    def getFirst(self):
        return self.__first
    def isEmpty(self): return self.__first is None
    def insertFirst(self, n): 
        n.setPrevious(None)
        n.setNext(self.__first)
        if self.isEmpty(): self.__first=self.__last=n
        else:
            self.__first.setPrevious(n)
            self.__first=n
    def deleteLast(self):
        last=self.__last
        if last is None: return None
        newLast=self.__last.getPrevious()
        if newLast is None: self.__first=self.__last=None
        else:
            last.setPrevious(None)
            newLast.setNext(None)
            self.__last=newLast
        return last
    def remove(self,node):
        if node is None: return None
        next=node.getNext()
        prev=node.getPrevious()
        if prev is None and next is None:
            self.__first=None
            self.__last=None
        elif prev is None:
            next.setPrevious(None)
            self.__first=next
        elif next is None:
            prev.setNext(None)
            self.__last=prev
        else:
            prev.setNext(next)
            next.setPrevious(prev)
        node.setNext(None)
        node.setPrevious(None)
        return node

class LRUcache(object):
    def __init__(self, capacity):
        self.__DLL=DLL()
        self.__size=0
        self.__capacity=capacity
        self.__map=dict()
        self.hits=0
        self.misses=0
    def __str__(self):
        return str(self.__DLL)
    def get(self,key):
        if key not in self.__map:
            self.misses+=1
            return None
        n=self.__map[key]
        self.__DLL.remove(n)
        self.__DLL.insertFirst(n)
        self.hits+=1
        return n.getData()
    def add(self,key,data):
        if key in self.__map:
            n=self.__map[key]
            n.setData(data)
            self.__DLL.remove(n)
            self.__DLL.insertFirst(n)
            return True
        n=Link(key,data)
        self.__map[key]=n
        if self.__size==self.__capacity:
            last=self.__DLL.deleteLast()
            if last:
                del self.__map[last.getKey()]
                self.__size-=1
        self.__DLL.insertFirst(n)
        self.__size+=1
        return True
            
            
def main():
    cache=LRUcache(10)
    keys=['A','B','C','D','E','F','G','H','A','D','E','G','Q','G','G']
    for key in keys:
        if cache.get(key) is None:
            cache.add(key,ord(key)*7)
    print("Hit rate:",cache.hits/(cache.hits+cache.misses))

if __name__=="__main__":
    main()