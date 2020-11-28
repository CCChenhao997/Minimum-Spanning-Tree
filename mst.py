# -*- coding: UTF-8 -*-
'''
Description: Project for CSE5311
version: 
Author: chenhao
Date: 2020-11-16 15:58:00
'''

import copy
import heapq
from collections import defaultdict
from utils import readGraphData, get_parse

class MST(object):
    def __init__(self, opt, edgelist, nodelist):
        self.opt = opt
        self.edgelist = edgelist
        self.nodelist = nodelist
        self.nodenum = len(nodelist)  
        self.nodedict = dict()
        for idx, node in enumerate(nodelist):
            self.nodedict[node] = idx
            
        self.set_nodes = []
        for node in nodelist:
            self.set_nodes.append({'name': node, 'value': 100, 'category': 0})

    def originGraph(self):
        if self.opt.terminal:
            return self.edgelist
        
        set_links = []
        for triple in self.edgelist:
            source, target, name = triple[0], triple[1], triple[2]
            source = self.nodedict[source]
            target = self.nodedict[target]
            set_links.append({'source': source, 'target': target, 'name': name})
        
        graph = {
            'type': 'force', 
            'nodes': self.set_nodes, 
            'links': set_links
        }
        return graph

    def primTree(self):
        """
            Prim minimum spanning tree
            return dict({
                        'type': 'force', 
                        'nodes': [{'name': node, 'value': 100, 'category': 0}, ...], 
                        'links': [{'source': source, 'target': target, 'name': weight}, ...]
                    })
        """
        res = []
        prim_candidate_node = copy.deepcopy(self.nodelist)
        prim_selected_node = []
        prim_selected_node.append(prim_candidate_node[0])
        prim_candidate_node.remove(prim_selected_node[0])
        
        while len(prim_candidate_node) > 0:
            edge_weight = dict()
            node1 = None
            node2 = None
            weight = None
            for i in prim_selected_node:        # source node
                for j in prim_candidate_node:   # target node
                    for edge in self.edgelist:
                        if (edge[0] == i and edge[1] == j) or (edge[0] == j and edge[1] == i) :
                            edge_weight[i + '-' + j] = edge[2]
            # print(edge_weight)  # {'A-B': 2.0, 'A-C': 3.0}
            nodes_weight = sorted(edge_weight.items(), key=lambda kv:(kv[1], kv[0]))[0]
            node1 = nodes_weight[0].split('-')[0]
            node2 = nodes_weight[0].split('-')[1]
            weight = nodes_weight[1]
            res.append([node1, node2, weight])  # 然后将选取的最小权值的边加入到最小生成树中即可
            prim_selected_node.append(node2)
            prim_candidate_node.remove(node2)
        
        if self.opt.terminal:
            return res
        
        set_links = []
        for triple in res:
            source, target, weight = triple[0], triple[1], triple[2]
            source = self.nodedict[source]
            target = self.nodedict[target]
            set_links.append({'source': source, 'target': target, 'name': weight})
        
        prim_tree = {
            'type': 'force', 
            'nodes': self.set_nodes, 
            'links': set_links
        }
        return prim_tree

    def primTreeWithHeap(self):
        """
            Prim minimum spanning tree
            return dict({
                        'type': 'force', 
                        'nodes': [{'name': node, 'value': 100, 'category': 0}, ...], 
                        'links': [{'source': source, 'target': target, 'name': weight}, ...]
                    })
        """
        res = []
        nodes_neighbors = defaultdict(list)
        for node1, node2, weight in self.edgelist:
            nodes_neighbors[node1].append((weight, node1, node2))
            nodes_neighbors[node2].append((weight, node2, node1))
        
        nodelist = copy.deepcopy(self.nodelist)
        all_nodes = set(nodelist)
        used_nodes = set([nodelist[0]])
        usable_edges = nodes_neighbors[nodelist[0]][:]  # [('6', 'V1', 'V2'), ('1', 'V1', 'V3'), ('5', 'V1', 'V4')]
        heapq.heapify(usable_edges)
        
        while usable_edges and (all_nodes - used_nodes):
            weight, node1, node2 = heapq.heappop(usable_edges)
            if node2 not in used_nodes:
                used_nodes.add(node2)
                res.append([node1, node2, weight])
                
                for edge in nodes_neighbors[node2]:
                    if edge[2] not in used_nodes:
                        heapq.heappush(usable_edges, edge)
        
        if self.opt.terminal:
            return res
        
        set_links = []
        for triple in res:
            source, target, weight = triple[0], triple[1], triple[2]
            source = self.nodedict[source]
            target = self.nodedict[target]
            set_links.append({'source': source, 'target': target, 'name': weight})
        
        prim_tree = {
            'type': 'force', 
            'nodes': self.set_nodes, 
            'links': set_links
        }
        return prim_tree
    
    def kruskalTree(self):
        """
            Kruskal minimum spanning tree
            return dict({
                        'type': 'force', 
                        'nodes': [{'name': node, 'value': 100, 'category': 0}, ...], 
                        'links': [{'source': source, 'target': target, 'name': weight}, ...]
                    })
        """

        # find the root node of a node
        def findRoot(node):
            if unicon_dict[node] != node:
                unicon_dict[node] = findRoot(unicon_dict[node])
            return unicon_dict[node]

        # merge two unicon
        def mergeConnectedComponent(node1, node2):
            root1 = findRoot(node1)
            root2 = findRoot(node2)
            if root1 != root2:
                if layer_dict[root1] > layer_dict[root2]:
                    unicon_dict[root2] = root1
                else:
                    unicon_dict[root1] = root2
                    if layer_dict[root1] == layer_dict[root2]:
                        layer_dict[root2] += 1

        unicon_dict = dict()
        layer_dict = dict()
        
        for node in self.nodelist:
            unicon_dict[node] = node
            layer_dict[node] = 0
        
        res = []
        edgelist = self.edgelist
        edgesorted = sorted(edgelist, key=lambda weight: weight[2])
        for edge in edgesorted:
            node1, node2, weight = edge
            if findRoot(node1) != findRoot(node2):
                mergeConnectedComponent(node1, node2)
                res.append(edge)

        if self.opt.terminal:
            return res
        
        set_links = []
        for triple in res:
            source, target, weight = triple[0], triple[1], triple[2]
            source = self.nodedict[source]
            target = self.nodedict[target]
            set_links.append({'source': source, 'target': target, 'name': weight})
        
        kruskal_tree = {
            'type': 'force',
            'nodes': self.set_nodes, 
            'links': set_links
        }
        return kruskal_tree




if __name__ == "__main__":
    # edgelist = [['V1', 'V2', '6'], ['V1', 'V3', '1'], ['V1', 'V4', '5'], 
    #             ['V2', 'V3', '5'], ['V2', 'V5', '3'], ['V3', 'V4', '5'], 
    #             ['V3', 'V5', '6'], ['V3', 'V6', '4'], ['V4', 'V6', '2'], 
    #             ['V5', 'V6', '6']]
    # nodelist = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6']
    
    opt = get_parse()
    edgelist, nodelist = readGraphData(opt.data_path)
    mst = MST(opt, edgelist, nodelist)
    if opt.mst == 'prim':
        print("---------------Prim Tree---------------")
        print(mst.primTree())
    elif opt.mst == 'prim_with_heap':
        print("---------------Prim Tree with Heap---------------")
        print(mst.primTreeWithHeap())
    elif opt.mst == 'kruskal':
        print("---------------Kruskal Tree---------------")
        print(mst.kruskalTree())
    
    if opt.graph:
        print("---------------Original Graph---------------")
        print(mst.originGraph())