import unittest
import recursive_tree

class lbtypes_test(unittest.TestCase):
    def test_values(self):
        root = recursive_tree.node('root')
        root.create_child('node1','node2','node3')
        root.childs['node1'].value = 1
        root.childs['node2'].value = 2
        root.childs['node3'].value = 3
        self.assertEqual(root.childs['node1'].value,1)
        self.assertEqual(root.childs['node2'].value,2)
        self.assertEqual(root.childs['node3'].value,3)
        self.assertEqual(root.value,6)
        
    def test_meta(self):
        root = recursive_tree.node('root')
        root.create_child('node1','node2','node3')
        root.childs['node1'].meta['attr'] = 1
        root.childs['node2'].meta['attr'] = 2
        root.childs['node3'].meta['attr'] = 3
        self.assertEqual(root.childs['node1'].meta['attr'],1)
        self.assertEqual(root.childs['node2'].meta['attr'],2)
        self.assertEqual(root.childs['node3'].meta['attr'],3)
        self.assertFalse(root.meta.has_key('attr'))

    def test_grand_childs(self):
        root = recursive_tree.node('root')
        root.create_child('node1','node2')
        root.childs['node1'].create_child('node11','node12')
        root.childs['node2'].create_child('node21','node22')
        root.childs['node1'].childs['node11'].create_child('node111','node112')
        root.childs['node2'].childs['node21'].create_child('node211','node212')
        childs = [child.name for child in root.grand_childs(0)]
        grand_childs = [child.name for child in root.grand_childs(1)]
        grand_grand_childs = [child.name for child in root.grand_childs(2)]
        
        self.assertIn('node1',childs)
        self.assertIn('node2',childs)
        self.assertIn('node11',grand_childs)
        self.assertIn('node12',grand_childs)
        self.assertIn('node21',grand_childs)
        self.assertIn('node22',grand_childs)
        self.assertIn('node111',grand_grand_childs)
        self.assertIn('node112',grand_grand_childs)
        self.assertIn('node211',grand_grand_childs)
        self.assertIn('node212',grand_grand_childs)
        
if __name__ == '__main__':
    unittest.main()