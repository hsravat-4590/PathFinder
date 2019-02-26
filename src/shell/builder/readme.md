# Builder Library

The Builder Library contains classes used to build a node graph.

## Commands:
``pathfinder build new <name-of-graph> `` : Used to mark the creation of a new node tree. you can use `-h` if you want to support heuristics in the model.

* For the following commands to work you will need to select a node tree using the select command

``pathfinder tree append <nodename> <[[connected node, distance, heuristic]]>``: you can add as many connections in the array as you like and heuristics will only be considered if the USE_HEURISTIC switch is applied.

`pathfinder tree remove-node <nodename>` : Remove a node and all of its links

`pathfinder tree remove-node-connection <node> <connection>` : Breaks a link from a node and a connection

`pathfinder build tree` : Builds the tree into a JSON format and does a check to ensure that all nodes can be accessed.
