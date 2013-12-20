/**
Program to create a trinary tree, perform node insertion and deletion operations.
**/

class TrinaryTreeNode
{
    // Creates trinary tree node with given value 
    
    int val;
    TrinaryTreeNode left;
    TrinaryTreeNode middle;
    TrinaryTreeNode right;

    public TrinaryTreeNode(int val)
    {
        this.val = val;
        this.left = this.middle = this.right = null;
    }
}

class FullTrinaryTree
{
    public TrinaryTreeNode insert(int val, TrinaryTreeNode node)
    {
        // Node insertion function
        if (node == null)
        {
            node = new TrinaryTreeNode(val);
        }
        else if (val < node.val)
        {
            node.left = insert(val, node.left);
        }
        else if ( val == node.val)
        {
            node.middle = insert(val, node.middle);
        }
        else 
        {
            node.right = insert(val, node.right);
        }
        return node;
    }

    public int findSuccessor(TrinaryTreeNode node)
    {
        //Find the successor of the given node
        if (node != null)
        {
            while (node.left != null)
            {
                return findSuccessor(node.left);
            }
        }
        return node.val;
    }

    public TrinaryTreeNode delete(int val, TrinaryTreeNode node)
    {
        // Node deletion function 
        if (node == null)
        {
            throw new RuntimeException();
        }
        else if(val < node.val)
        {
            node.left = delete(val, node.left);    
        }
        else if (val > node.val)
        {
            node.right = delete(val, node.right);
        }
        else
        {
            if (node.middle != null)
            {
                node.middle = delete(val, node.middle);
            }
            
            else if (node.right != null)
            {
                //Find the successor of the node
                node.val = findSuccessor(node.right);
                node.right = delete(findSuccessor(node.right), node.right);
            }
            else
            {
                node  = node.left;
            }
        }
        return node;
    }

    public void display(TrinaryTreeNode node)
    {
        //Print the tree node values
        if (node == null)
            return;
        display(node.left);
        System.out.println(node.val);
        display(node.middle);
        display(node.right);
    }
}

//Main class
public class TrinaryTree
{
    public static void main(String[] args)
    {
        FullTrinaryTree tree = new FullTrinaryTree();
        TrinaryTreeNode root = null;

        //Insertion
        root = tree.insert(10, root);
        root = tree.insert(28, root);
        root = tree.insert(8, root); 
        root = tree.insert(23, root);
        root = tree.insert(7, root); 
        
        //Print tree
        System.out.println("Tree before deletion");
        tree.display(root);

        //Deletion
        root = tree.delete(23, root);

        //Print tree
        System.out.println("Tree after deletion");
        tree.display(root);    
    }
}
