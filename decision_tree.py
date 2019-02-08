


class Node(object):
    """
    A class for a tree node
    This class is specifically for a decision-type tree
    """
    
    def __init__(self, name='root', attribute=None, action=None, parent=None, branches=None):
        self.name = name
        self.attribute = attribute
        self.action = action
        self.parent = parent
        self.branches = {}
    
    def __repr__(self):
        return self.name
    
    def add_branch(self, value, node=None):
        self.branches[value] = node
        
    def get_branch(self, value):
        return self.branches[value]
    
    def print_tree(self):
        print("Type = " + self.name)
        if self.attribute is not None:
            print("Attribute = " + self.attribute)
        if self.parent is not None:
            print("Parent = " + self.parent)
        if self.action is not None:
            print("Action = " + self.action)
        if len(self.branches) > 0:
            for branch in self.branches:
                print("\n")
                print("Value = " + branch)
                self.branches[branch].print_tree()



def majority_label(S, attribute="label", replace=False):
    """
    Determines the majority label of a given attribute.
    
    Input: 
    S:  A list of dictionaries with key-value pairs represented as strings.
    attribute: The attribute that will be searched 
    replace:  If replace is True, the value "unknown" will not be counted in determing the majority label
    
    Returns:  a string representing the most common value in the list for the key attribute 
    """
    counts = {}
    
    for s in S:
        value = s[attribute]
        if value in counts:
            if value != "unknown":
                counts[value] += 1
            else:
                if not replace:
                    counts[value] += 1    
        else:
            if value != "unknown":
                counts[value] = 1
            else:
                if not replace:
                    counts[value] = 1   
    
    return max(counts, key=counts.get)



def read_file(path, label):
    """
    Reads and processes a csv file for use in a decision tree algorithm.
    
    Input: 
    -path: a string representing the file path of the csv file to be opened.  
    -label: represents the type of examples to be processed.  One of three possible values: "car","bank","tennis"
    

    Returns:  
    -S: a list of dictionaries.  Each dictionary represents a single instance (or one line in the data file)
        with key-value pairs representing attributes and values.      
    """    
    
    S = []
    with open(path, 'r') as f:
        for line in f:
            terms = line.strip().split(',')
                
            if label == "car":
                if len(terms) == 7:
                    example = {}
                    example["buying"] = terms[0]
                    example["maint"] = terms[1]
                    example["doors"] = terms[2]
                    example["persons"] = terms[3]
                    example["lug_boot"] = terms[4]
                    example["safety"] = terms[5]
                    example["label"] = terms[6]
                    S.append(example)
            
            if label == "bank":
                    
                if len(terms) == 17:
                    example = {}
                    example["age"] = terms[0]
                    example["job"] = terms[1]
                    example["marital"] = terms[2]
                    example["education"] = terms[3]
                    example["default"] = terms[4]
                    example["balance"] = terms[5]
                    example["housing"] = terms[6]
                    example["loan"] = terms[7]
                    example["contact"] = terms[8]
                    example["day"] = terms[9]
                    example["month"] = terms[10]
                    example["duration"] = terms[11]
                    example["campaign"] = terms[12]
                    example["pdays"] = terms[13]
                    example["previous"] = terms[14]
                    example["poutcome"] = terms[15]
                    example["label"] = terms[16]
                    S.append(example)
                    
            if label == "tennis":
                if len(terms) == 5:
                    example = {}
                    example["outlook"] = terms[0]
                    example["temp"] = terms[1]
                    example["humidity"] = terms[2]
                    example["wind"] = terms[3]
                    example["label"] = terms[4]
                    S.append(example)
                    
    return S
            


def process_bank_data(S, mode, train_medians=None, replace=False, maj_values=None):
    """
    A function that processes the bank data.  First, it turns the numerical range into binary data.  
    The binary values ("high", "low") are based on a threshold. The threshold is the median value in the set S.
    Also, it can replace "unknown" attribute values with the majority value for that attribute.
        
    Inputs:
    -S: Set of data instances from the bank data set. 
    -mode: One of two types: "train" or "test".  If "train", medians will be calculated from data.
        If "test", the medians will be provided in the function call.
    -train_medians: dictionary with key-value pairs being the attribute and its associated numerical median.
    -replace:  If False, "unknown" attribute values are considered a value.  Otherwise if True, "unknown" 
               attribute values are replaced with the majority value of that attribute.
    -maj_labels:  a dictionary with key-value pairs being the attribute and its majority label.
    
    Returns:
    -medians:  A dictionary with key-value pairs.  The key is the attribute represented as a string and 
        the value is the corresponding numerical median.
    -majority: A dictionary with key-value pairs .  The key is the attribute represented as a string and 
        the value is the corresponding majority element for that attribute
    """

    from statistics import median
    
    #Calculate the median if training mode
    if mode == "train":
        age = []
        balance = []
        day = []
        duration = []
        campaign = []
        pdays = []
        previous = []
    
        for s in S:
            age.append(int(s["age"]))
            balance.append(int(s["balance"]))
            day.append(int(s["day"]))
            duration.append(int(s["duration"]))
            campaign.append(int(s["campaign"]))
            pdays.append(int(s["pdays"]))
            previous.append(int(s["previous"]))
        
        age.sort()
        balance.sort()
        day.sort()
        duration.sort()
        campaign.sort()
        pdays.sort()
        previous.sort()
        
        med_age = median(age)
        med_balance = median(balance)
        med_day = median(day)
        med_duration = median(duration)
        med_campaign = median(campaign)
        med_pdays = median(pdays)
        med_previous = median(previous)
        maj_job = majority_label(S,"job", "True")
        maj_education = majority_label(S, "education", "True")
        maj_contact = majority_label(S, "contact", "True")
        maj_poutcome = majority_label(S, "poutcome", "True")
    
    else:
        med_age = train_medians["age"]
        med_balance = train_medians["balance"]
        med_day = train_medians["day"]
        med_duration = train_medians["duration"]
        med_campaign = train_medians["campaign"]
        med_pdays = train_medians["pdays"]
        med_previous = train_medians["previous"]
        maj_job = maj_values["job"]
        maj_education = maj_values["education"]
        maj_contact = maj_values["contact"]
        maj_poutcome = maj_values["poutcome"]


    for s in S:
        s["age"] = "high" if s["age"] > med_age else "low"
        s["balance"] = "high" if s["balance"] > med_balance else "low"
        s["day"] = "high" if s["day"] > med_day else "low"
        s["duration"] = "high" if s["duration"] > med_duration else "low"
        s["campaign"] = "high" if s["campaign"] > med_campaign else "low"
        s["pdays"] = "high" if s["pdays"] > med_pdays else "low"
        s["previous"] = "high" if s["previous"] > med_previous else "low"
        if replace:
            if s["job"] == "unknown":
                s["job"] = maj_job 
            if s["education"] == "unknown":
                s["education"] = maj_education
            if s["contact"] == "unknown":
                s["contact"] = maj_contact 
            if s["poutcome"] == "unknown":
                s["poutcome"] = maj_poutcome

        
    medians = {
        "age": med_age,
        "balance": med_balance,
        "day": med_day,
        "duration": med_duration,
        "campaign": med_campaign,
        "pdays": med_pdays,
        "previous": med_previous
    }
    
    majority = {
        "job": maj_job,
        "education": maj_education,
        "contact": maj_contact,
        "poutcome": maj_poutcome
    }

    return S, medians, majority


def create_attribute_dictionary(example_type, replace=False):
    """
    Creates a master dictionary for the attributes that are used for learning a decision tree.
    This is a convenience function and will vary for each type of problem.
    Currently this function supports three types of datasets:  "car", "bank", and "tennis".
    The key is a string and represents a particular attribute in the sample data.
    The value is a tuple of strings and represents all possible values that the attribute can take.
    
    Inputs:
    -example_type:   "car" -- represents the car data example
                    "bank" -- represents the bank data example
                    "tennis" -- represents tennis game example used for testing implementation
    -replace:  If False, "unknown" attribute values are considered a value.  Otherwise if True, "unknown" 
               attribute values are replaced with the majority value of that attribute.
    Returns:
    -attributes:  a dictionary of attributes and values
    """
    
    if example_type == "car":
        attributes = {
            "buying":("vhigh", "high", "med", "low"),
            "maint":("vhigh", "high", "med", "low"),
            "doors":("2", "3", "4", "5more"),
            "persons":("2", "4", "more"),
            "lug_boot":("small", "med", "big"),
            "safety":("low", "med", "high"),
            "label":("unacc", "acc", "good", "vgood")
        }
        
    if example_type == "bank":
        attributes = {
            "age": ("high", "low"),
            "marital": ("married", "divorced", "single"),
            "default": ("yes", "no"),
            "balance": ("high", "low"),
            "housing": ("yes", "no"),
            "loan": ("yes", "no"),
            "day":("high", "low"),
            "month":("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", 
                     "sep", "oct", "nov", "dec"),
            "duration": ("high", "low"),
            "campaign": ("high", "low"),
            "pdays": ("high", "low"),
            "previous": ("high", "low"),
            "label": ("yes", "no")
        }
        
        if not replace:
            attributes["job"] = ("admin.", "unknown", "unemployed", "management", "housemaid",
                    "entrepreneur", "student", "blue-collar", "self-employed", 
                    "retired", "technician","services")
            attributes["education"] = ("unknown", "secondary","primary","tertiary")
            attributes["contact"] = ("unknown","telephone","cellular")
            attributes["poutcome"] = ("unknown", "other", "failure", "success")
        else:
            attributes["job"] = ("admin.", "unemployed", "management", "housemaid",
                    "entrepreneur", "student", "blue-collar", "self-employed", 
                    "retired", "technician","services")
            attributes["education"] = ("secondary","primary","tertiary")
            attributes["contact"] = ("telephone","cellular")
            attributes["poutcome"] = ("other", "failure", "success")
        
    if example_type == "tennis":
        attributes = {
            "outlook":("sunny","overcast","rainy"),
            "temp":("hot","medium","cool"),
            "humidity":("high","normal","low"),
            "wind":("strong","weak"),
            "label":("yes","no")
        }
    
    return attributes


def entropy(S):
    """
    Calculates the entropy of a given dataset S.
    
    Input:
    -S: A list of dictionaries with key-value pairs represented as strings. 
    
    Returns:
    -entropy:  A float, which is the calculated entropy for the key 'label'.
    """
    
    import math
    
    #Iterate through list to count the different labels
    counts = {}
    if len(S) == 0:
        return 0.0
    for s in S:
        value = s['label']
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    entropy = 0.0
    total_count = len(S)
    for count in counts.values():
        ratio = float(count) / total_count
        entropy += -1 * ratio * math.log(ratio,2)
    
    return entropy
        


def majority_error(S):
    """
    Calculates the majority error of a given dataset S.
    
    Input:
    -S: A list of dictionaries with key-value pairs represented as strings. 
    
    Returns:
    -majority_error:  A float, which is the calculated majority error for the key 'label'.
    """
    
    import math
    
    #Iterate through list to count the different labels
    counts = {}
    if len(S) == 0:
        return 0.0
    for s in S:
        value = s['label']
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    majority = max(counts.values())
    total_count = len(S)
    majority_error = 1 - float(majority) / total_count
    return majority_error
        


def gini_index(S):
    """
    Calculates the gini index for a given dataset S.
    
    Input:
    -S: A list of dictionaries with key-value pairs represented as strings. 
    
    Returns:
    -gini:  A float, which is the calculated gini index for the key 'label'.
    """
    
    import math
    
    #Iterate through list to count the different labels
    counts = {}
    if len(S) == 0:
        return 0.0
    for s in S:
        value = s['label']
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    total_count = len(S)
    gini = 0.0
    for count in counts.values():
        ratio = float(count) / total_count
        gini += ratio**2
    
    return 1 - gini
        

def best_attribute(S, Attributes, master_list, error_type):
    """
    Determines the attribute A that produces the greatest information gain amongst a set of attributes.
    The information gain is determined by the error_type.
    
    Input:
    -S:  A list of examples, which are dictionaries of key-values represented attributes and values respectively.
    -Attributes:  A set of attributes that will be compared
    -master_list: A dictionary, which contains all the possible values each attribute can have
    error_type:  One of three types:  "entropy", "me" (majority error) or "gini" (gini index)
    
    returns:
    -A:  a string that is the attribute with the largest information gain in the given dataset S. 
    """
    
    information_gain = {}
    
    if error_type == "entropy":
        current_entropy = entropy(S)
    if error_type == "me":
        current_entropy = majority_error(S)
    if error_type == "gini":
        current_entropy = gini_index(S)

    #Iterate through all attributes
    #If the sample s has the given value for the attribute, add it to the list
    for attribute in Attributes:
        expected_entropy = 0.0

        for value in master_list[attribute]:
            current_value = []
            for s in S:
                if s[attribute] == value:
                    current_value.append(s)
            if error_type == "entropy":
                value_entropy = entropy(current_value)
            if error_type == "me":
                value_entropy = majority_error(current_value)
            if error_type == "gini":
                value_entropy = gini_index(current_value)

            ratio = float(len(current_value)) / len(S)
            expected_entropy += ratio * value_entropy
                #print("Expected entropy of " + attribute + " is " + str(expected_entropy))
        
        information_gain[attribute] = current_entropy - expected_entropy
        
    return max(information_gain, key=information_gain.get)
    


def ID3(S, Attributes, master_list, error_type, current_depth, max_depth):
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

    returns:
    -root_node:  A tree node
    """
    
    if current_depth == max_depth:
        label = majority_label(S)
        return Node(name='leaf', action=label)
    sample_size = len(S)
    
    #Test all labels to see if they are the same
    label = S[0]["label"]
    count = 0
    for s in S:
        if s["label"] != label:
            break
        else:
            count = count + 1
    
    if count == sample_size:
        
        #If attributes is empty, return a leaf node with the most common label
        if len(Attributes) == 0:
            label = majority_label(S)
        return Node(name='leaf', action=label)
    
    else:
        root_node = Node()
        A = best_attribute(S, Attributes, master_list, error_type)
        root_node.attribute = A
        if A in Attributes:
            Attributes.remove(A)
        
        for value in master_list[A]:
            
            #Create new subset of examples
            S_v = []
            for sample in S:
                if sample[A] == value:
                    S_v.append(sample)
            
            if len(S_v) == 0:
                maj_label = majority_label(S)
                new_node = Node(name="leaf", attribute=A, parent=root_node.attribute, action=maj_label)
                
            else:                
                new_node = ID3(S_v, Attributes, master_list, error_type, current_depth+1, max_depth)
                new_node.parent = root_node.attribute
            root_node.add_branch(value, new_node)
            
        #Add attribute removed from list so that next iteration of recursive call has the correct attribute set
        Attributes.add(A)
            
                
    return root_node
    

def build_decision_tree(path, example, purity_type, max_depth, replace=False):
    """
    Creates a decision tree from the given dataset and parameters
    
    Inputs:
    -path:  A string, representing the path of the dataset to be processed.
    -example:  One of three types:  "bank", "car", "tennis".  Represents the type of dataset to be used.
    -purity_type:  One of three types:  "entropy", "me" and "gini".  Represents how information gain will be
        calculated in the decision tree.
    -max_depth:  The maximum depth of the decision tree
    -replace:  If False, "unknown" attribute values are considered a value.  Otherwise if True, "unknown" 
               attribute values are replaced with the majority value of that attribute.
               
    Returns:
    -tree:  A decision tree
    -medians:  A dictionary with key-value pairs.  The key is the attribute represented as a string and 
        the value is the corresponding numerical median.  This is only returned when "bank" is the example type.
        Otherwise, None is returned.
    -majority: A dictionary with key-value pairs .  The key is the attribute represented as a string and 
        the value is the corresponding majority element for that attribute.  This is only returned when "bank" 
        is the example type.  Otherwise, None is returned.

    """
    
    S = read_file(path, example)

    medians = majority = None
    if example == "bank":
        S, medians, majority = process_bank_data(S, "train", replace)
    master_list = create_attribute_dictionary(example, replace)
    Attributes = set(list(master_list.keys()))
    Attributes.remove("label")
    
    return ID3(S, Attributes, master_list, purity_type, 0, max_depth), medians, majority


def walk_tree(node, s):
    """
    Recurisive function.  Given an example s walks through a tree, following the branch of each 
    node with the given value in s.  
    
    Inputs:  
    -node:  A tree node.
    -s: One data instance containing attributes and vaues.
    
    Return:
    -action:  A string, representing the action of the leaf node.
    """
    
    value = s[node.attribute]
    next_node = node.get_branch(value)
    if next_node.name == "root":
        action = walk_tree(next_node, s)
    else:
        #At leaf node
        action = next_node.action
    
    return action


def test_decision_tree(tree, path, example, medians=None, majority=None, replace=False):
    """
    With a given decision tree, tests the decision tree for accuracy against a given data set.
    
    Inputs:
    -tree:  The decision tree to be tested.
    -path:  A string, representing the path of the dataset that will be used for testing the decision tree.
    -example:  One of three types:  "bank", "car" and "tennis".  Represents the type of dataset to be used.
    -medians:  A dictionary with key-value pairs. The key is the attribute represented as a string and 
        the value is the corresponding numerical median.  This is only used for the "bank" data.
    -majority: A dictionary with key-value pairs. The key is the attribute represented as a string and 
        the value is the corresponding majority element for that attribute. This is only use for the "bank" data. 
    -replace:  If False, "unknown" attribute values are considered a value.  Otherwise if True, "unknown" 
               attribute values are replaced with the majority value of that attribute.
               
    Returns:
    -ratio:  A float, representing the error rate of the decision tree with the given dataset.
    """
    
    S = read_file(path, example)
    
    if example == "bank":
        S,_,_ = process_bank_data(S, "test", train_medians=medians, maj_values=majority, replace=replace)
    
    #itereate through each item of list.  Keep track of correct classifications and incorrect classfications
    correct = incorrect = 0
    count = 1
    for s in S:
        action = walk_tree(tree, s)
        if action == s["label"]:
            correct += 1
        else:
            incorrect += 1
        count += 1
            
    #print("The number correct is " + str(correct) + " and the number incorrect is " + str(incorrect))
    ratio = float(correct) / len(S)
    return ratio



def test_car():
    
    print("Testing car dataset: ")
    print("\n")
    
    for i in range(1,7):
        for purity_type in {"entropy", "me", "gini"}:
            print("Results with tree depth of " + str(i) + " using purity type = " + str(purity_type) + " :")
            tree, _, _ = build_decision_tree("car/train.csv", "car", purity_type, i, replace=False)
            ratio_train = test_decision_tree(tree, "car/train.csv", "car")
            ratio_test = test_decision_tree(tree, "car/test.csv", "car")
            print("The average prediction error for the training set is " + "{:.2f}".format(1-ratio_train)
              + " and the error for the testing set is " + "{:.2f}".format(1-ratio_test))
        print("\n")


def test_bank():
    
    print("Testing bank dataset: ")
    print("\n")
    
    for i in range(1,17):
        for purity_type in {"entropy", "me", "gini"}:
            for replace in (True,False):
                print("Results with tree depth of " + str(i) + " using purity type = " + str(purity_type) + 
                      " and replace = " + str(replace) + " :")
                #print("test" + str(replace))
                tree, medians, majority = build_decision_tree("bank/train.csv", "bank", purity_type, i, replace=replace)
                ratio_train = test_decision_tree(tree, "bank/train.csv", "bank", medians=medians, 
                                                 majority=majority, replace=replace)
                ratio_test = test_decision_tree(tree, "bank/test.csv", "bank", medians=medians, 
                                                 majority=majority, replace=replace)
                print("The average prediction error for the training set is " + "{:.2f}".format(1-ratio_train)
                      + " and the error for the testing set is " + "{:.2f}".format(1-ratio_test))
                print("\n")


test_car()
print("\n")
test_bank()



