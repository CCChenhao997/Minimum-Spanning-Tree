# -*- coding: UTF-8 -*-
'''
Description: 
version: 
Author: chenhao
Date: 2020-11-17 14:53:04
'''
import time
import json
from mst import MST
from utils import get_parse
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

graph_info = None
prim_tree = None
kruskal_tree = None
start = None

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/graph', methods=['POST', 'GET'])
def get_graph():
    global start
    global graph_info
    if request.method == 'POST':
        start = time.time()
        input_data = request.get_data()
        if isinstance(input_data, bytes):
            input_data = str(input_data, encoding='utf-8')
        input_json = json.loads(input_data)
        edgelist = []
        nodesets = set()
        triple_list = input_json['text'].strip().split('\n')
        assert len(triple_list) != 1 and triple_list[0] != '', 'The input is empty!'
        for i in triple_list:
            edge = i.split('-')
            edgelist.append(edge)
            
            print(edge)
            nodesets.add(edge[0])
            nodesets.add(edge[1])
        nodelist = list(nodesets)
        # nodelist.sort()
        opt = get_parse()
        mst = MST(opt, edgelist, nodelist)
        graph_info = mst.originGraph()
        difftime = time.time() - start
        print("Time consumption of generating graph is {:.5f} second".format(difftime))
        
    if graph_info is None:
        print("Graph is none.")
        exit()
    
    return jsonify(graph_info)
    
@app.route('/prim', methods=['POST', 'GET'])
def get_prim_tree():
    global start
    global prim_tree
    if request.method == 'POST':
        start = time.time()
        input_data = request.get_data()
        if isinstance(input_data, bytes):
            input_data = str(input_data, encoding='utf-8')
        input_json = json.loads(input_data)
        edgelist = []
        nodesets = set()
        triple_list = input_json['text'].strip().split('\n')
        assert len(triple_list) != 1 and triple_list[0] != '', 'The input is empty!'
        for i in triple_list:
            edge = i.split('-')
            edgelist.append(edge)
            nodesets.add(edge[0])
            nodesets.add(edge[1])
        nodelist = list(nodesets)
        # nodelist.sort()
        opt = get_parse()
        mst = MST(opt, edgelist, nodelist)
        prim_tree = mst.primTree()
        difftime = time.time() - start
        print("Time consumption of prim is {:.5f} second".format(difftime))
        
    if prim_tree is None:
        print("Graph is none.")
        exit()
        
    return jsonify(prim_tree)

@app.route('/prim_with_heap', methods=['POST', 'GET'])
def get_prim_tree_with_heap():
    global start
    global prim_tree
    if request.method == 'POST':
        start = time.time()
        input_data = request.get_data()
        if isinstance(input_data, bytes):
            input_data = str(input_data, encoding='utf-8')
        input_json = json.loads(input_data)
        edgelist = []
        nodesets = set()
        triple_list = input_json['text'].strip().split('\n')
        assert len(triple_list) != 1 and triple_list[0] != '', 'The input is empty!'
        for i in triple_list:
            edge = i.split('-')
            edgelist.append(edge)
            nodesets.add(edge[0])
            nodesets.add(edge[1])
        nodelist = list(nodesets)
        # nodelist.sort()
        opt = get_parse()
        mst = MST(opt, edgelist, nodelist)
        prim_tree = mst.primTreeWithHeap()
        difftime = time.time() - start
        print("Time consumption of prim_with_heap is {:.5f} second".format(difftime))
        
    if prim_tree is None:
        print("Graph is none.")
        exit()
        
    return jsonify(prim_tree)

@app.route('/kruskal', methods=['POST', 'GET'])
def get_kruskal_tree():
    global start
    global kruskal_tree
    if request.method == 'POST':
        start = time.time()
        input_data = request.get_data()
        if isinstance(input_data, bytes):
            input_data = str(input_data, encoding='utf-8')
        input_json = json.loads(input_data)
        edgelist = []
        nodesets = set()
        triple_list = input_json['text'].strip().split('\n')
        assert len(triple_list) != 1 and triple_list[0] != '', 'The input is empty!'
        for i in triple_list:
            edge = i.split('-')
            edgelist.append(edge)
            nodesets.add(edge[0])
            nodesets.add(edge[1])
        nodelist = list(nodesets)
        # nodelist.sort()
        opt = get_parse()
        mst = MST(opt, edgelist, nodelist)
        kruskal_tree = mst.kruskalTree()
        difftime = time.time() - start
        print("Time consumption of kruskal is {:.5f} second".format(difftime))
        
    if kruskal_tree is None:
        print("Graph is none.")
        exit()
        
    return jsonify(kruskal_tree)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)