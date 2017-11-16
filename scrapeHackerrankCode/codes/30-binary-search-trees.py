# Accepted
# Python 3

    def getHeight(self,root):
        if not root:
            return -1
        else:
            lheight = self.getHeight(root.left)
            rheight = self.getHeight(root.right)
            
            if lheight > rheight:
                return lheight+1
            else:
                return rheight+1
