# DecisionTree
This is a machine learning library developed by Janaan Lake for CS5350/6350 at University of Utah

Currently this library used two datasets.  The car evaulation datasets from https://archive.ics.uci.edu/ml/datasets/car+evaulation and the bank dataset from https://archive.ics.uci.edu/ml/datasets/Bank+Marketing.  

To run the decision tree libraries type the following on the command line:
python3 decision_tree.py

The decision tree incorporates three types of purity calculations:  information gain, majority error and gini index.  

The test_car() and test_bank() methods will create a single decision tree with varying depth levels and different purity types.  The accuracy results of all these is output.

The method that creates the decision tree is ID3.

ID3(S, Attributes, master_list, error_type, current_depth, max_depth=float('inf'), weighted=False):
    """
    Creates a decision tree using the ID3 algorithm.
    
    Inputs: 
    -S: list of dictionaries; each dictionary contains a set of key-value pairs that are strings.
        The key is a string representing the attribute, and the value is a string representing the value of that
        attribute.  Labels are included as an attribute in the dictionary.  
        Each dictionary represents one example.
    -Attributes: set of attributes.  These are the attributes that will be searched when building the tree.
    -master_list: A dictionary, which contains all the possible values each attribute can have
    -error_type:  One of three types:  "entropy", "me" (majority error) or "gini" (gini index)
    -current_depth:  The current depth of the decision tree being constructed.
    -max_depth:  The maximum depth of the tree to be constructed.
    -weighted:  Boolean value that represents whether the data is weighted

    returns:
    -root_node:  A tree node
    """
