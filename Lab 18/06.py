def get_bst_postorder(bst):

   postorder = []
   if bst.get_left() is not None:
       postorder.extend(get_bst_postorder(bst.get_left()))
   if bst.get_right() is not None:
       postorder.extend(get_bst_postorder(bst.get_right()))
   postorder.append(bst.get_data())
   return postorder