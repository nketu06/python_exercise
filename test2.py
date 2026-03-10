class Range:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start>=self.end:
            raise StopIteration
        curr = self.start
        self.start+=1
        return curr
    
r = Range(3,9)
for i in range(3,8):
    print(i)