from node import Node 

class Calculations():

    def __init__(self, node):
        self.node = node
        self.sum = None
        self.count = 0
        self.average = 0
        self.nodes = []
        self.median = 0

    def __call__(self):
        print("Sum: " + str(self.calculate_sum(self.node)))
        print("Average: " + str(self.calculate_average()))
        print("Median: " + str(self.calculate_median()))

    def calculate_sum(self, node):
        sum = node.value
        self.count += 1
        self.nodes.append(node)

        if node.left != None:
            sum += self.calculate_sum(node.left)
        if node.right != None:
            sum += self.calculate_sum(node.right)

        self.sum = sum
        return sum

    def calculate_average(self):
        if self.sum == None:
            self.calculate_sum(self.node)

        self.average = self.sum / self.count
        return self.average

    def calculate_median(self):
        length = len(self.nodes)
        if length == 0:
             self.calculate_sum(self.node)

        self.nodes.sort(key=lambda x: x.value)

        if length % 2 == 0:
            self.median = (self.nodes[int(length/2) - 1].value + self.nodes[int(length/2)].value) / 2
        else:
            self.median = self.nodes[int(length/2)].value
        return self.median