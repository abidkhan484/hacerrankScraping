# Accepted
# Python 3

    def levelOrder(self,root):
        queue = [root]
        while queue:
            print(queue[0].data, end=' ')
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            del queue[0]
