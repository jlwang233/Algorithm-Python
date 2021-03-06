# encoding=utf-8
# date:2016-10-03
# gaooz.com
# 深度优先遍历

# 图节点的定义
class GraphicsNode(object):
    def __init__(self, data, neighbors = None):
        self._data = data
        # 图中与该顶点有关系的顶点集合
        self._neighbors = neighbors

# 深度优先搜索遍历
# graphics是图中节点的列表集合
def DFSTraverse(graphics):
    for i in range(len(graphics)):
        graphics[i]._isTraverse = False # 标记为未被访问过
    # 遍历
    for i in range(len(graphics)):
        if graphics[i]._isTraverse is False:
            DFS(graphics[i])

def DFS(node):
    # 标记为已经访问过
    node._isTraverse = True
    # 访问
    print node._data,
    if node._neighbors is not None:
        for i in range(len(node._neighbors)):
            if node._neighbors[i]._isTraverse is False:
                DFS(node._neighbors[i])

''' test

if __name__ == "__main__":
    node1 = GraphicsNode(1, [])
    node2 = GraphicsNode(2, [])
    node3 = GraphicsNode(3, [])
    node4 = GraphicsNode(4, [])
    node5 = GraphicsNode(5, [])

    node1._neighbors = [node2, node3]
    node2._neighbors = [node1, node4, node5]
    node3._neighbors = [node1, node5]
    node4._neighbors = [node2]
    node5._neighbors = [node2, node3]

    graphics = [node1, node2, node3, node4, node5]
    DFSTraverse(graphics)
'''