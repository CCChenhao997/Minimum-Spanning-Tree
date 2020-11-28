## CSE 5311 DSGN & ANLY ALGORITHMS Project (Minimum Spanning Tree)

### Directory

```
.
├── README.md			# readme
├── Report.md			# report
├── Report.pdf		   # report
├── app.py				# flask service
├── assets				# images
│   ├── kruskal_tree.png
│   ├── original_graph.png
│   └── prim_tree.png
├── data					# test data
│   ├── test_1.txt
│   ├── test_2.txt
│   ├── test_3.txt
│   ├── test_4.txt
│   ├── test_5.txt
│   └── test_6.txt
├── mst.py				# Including minimum spanning tree algorithms
├── static				# static files
│   ├── echarts.js
│   └── jquery-3.4.1.min.js
├── templates			# html file
│   └── index.html
└── utils.py			# Including reading data, generating data and setting arguments
```



### Requirement

- Python 3.7
- flask==1.0.2
- json
- argparse



### Usage

1. Run the flask service: `python app.py`

2. Run at terminal:

   ```shell
   # Prim Tree
   python mst.py --terminal --path test_1.txt --mst prim
   
   # Prim Tree with Heap
   python mst.py --terminal --path test_1.txt --mst prim_with_heap
   
   # Kruskal Tree
   python mst.py --terminal --path test_1.txt --mst kruskal
   ```

   If you want to see the original graph, run:

   ```shell
   python mst.py --terminal --graph
   ```

   

### Tips

When you click the button of the corresponding method, the run time will be displayed on the terminal.

[Click here to see report](Report.md)