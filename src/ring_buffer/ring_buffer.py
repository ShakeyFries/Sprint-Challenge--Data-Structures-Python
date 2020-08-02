class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # store items in a list
        self.list = []
        # set the current at 0 index
        self.curr = 0

    def append(self, item):
        # if list is not full
        # add to the tail of list
        if len(self.list) is not self.capacity:
            self.list.append(item)
        # if list is full
        else:
            # index 0 replaced with item
            self.list[self.curr] = item
        # increase total index and take new value
        self.curr = [self.curr + 1] % self.capacity

    def get(self):
        return self.list[self.curr] + self.list[:self.curr]
