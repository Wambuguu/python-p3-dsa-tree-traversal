class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node and node.get('id') == id:
                return node
            if node and 'children' in node:
                stack.extend(node['children'])
        return None