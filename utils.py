'''
Description: 
version: 
Author: chenhao
Date: 2020-11-21 17:11:18
'''
import os
import argparse
import random
import string

def readGraphData(path):
    edgelist = []
    nodesets = set()
    with open(path, 'r') as f:
        for line in f.readlines():
            edge = line.strip().split('-')
            edgelist.append(edge)
            nodesets.add(edge[0])
            nodesets.add(edge[1])
    nodelist = list(nodesets)
    return edgelist, nodelist
    
def get_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='test_1.txt')
    parser.add_argument('--mst', type=str, default=None, choices=['prim', 'prim_with_heap', 'kruskal'])
    parser.add_argument('--graph', default=False, action='store_true')
    parser.add_argument('--terminal', default=False, action='store_true')
    opt = parser.parse_args()
    cur_path = os.path.abspath(os.path.dirname(__file__))
    opt.data_path = cur_path + '/data/' + opt.path
    return opt

def dataGen(path, node_nums, edge_nums):
    # random.seed(888)
    nodes_set = set()
    for i in range(9999999999999):
        node = ''.join(random.sample(string.ascii_letters, 3))
        nodes_set.add(node)
        if len(nodes_set) == node_nums:
            break
    
    # nodelist = list(nodes_set)
    edgelist = []
    flag = False
    usednode_set = set()
    for node1 in nodes_set:
        usednode_set.add(node1)
        for node2 in nodes_set - usednode_set:
            edgelist.append([node1, node2, str(random.randint(1, 100))])
            
            if len(edgelist) == edge_nums:
                flag = True
                break
        if flag:
            break
    
    with open(path, 'w') as f:
        for edge in edgelist:
            node1, node2, weight = edge[0], edge[1], edge[2]
            f.writelines(node1 + '-' + node2 + '-' + weight + '\n')
    print("Write succeeded!")

if __name__ == "__main__":
    path = './data/test_6.txt'
    node_nums = 100
    # edge_nums = node_nums
    edge_nums = node_nums * (node_nums - 1) // 2
    print(edge_nums)
    assert edge_nums <= node_nums * (node_nums - 1) // 2 \
            and edge_nums > (node_nums - 1) and node_nums > 0, 'node_nums or edge_nums is error!'
    dataGen(path, node_nums, edge_nums)