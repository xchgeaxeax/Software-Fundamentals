def create_bst_from_list(values):


 bst = BinarySearchTree(values[0])
 for value in values[1:]:
   bst.insert(value)

 return bst