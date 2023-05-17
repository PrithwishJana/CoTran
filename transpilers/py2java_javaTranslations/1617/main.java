class TreeNode {
    protected void init__ ( this , val ) {
        this . var val = val;
        this . var left = None;
        this . right = None;
    }
}
class Solution extends  object {
    public void isSubtree ( this , s , t ) {
        s_res = this . preorder ( s , true );
        t_res = this . preorder ( t , true );
        return t_res in s_res;
    }
    public void preorder ( this , root , isLeft ) {
        if (root is None) {
            if (isLeft) {
                return "lnull";
            }
             else{
                return "rnull";
            }
        }
         return ";//" + str ( root . val ) + " " + this . preorder ( root . left , true ) + " " + this . preorder ( root . right , false )
    }
}

if (__name__ == "__main__") {
    sObj = Solution ( );
    root = TreeNode ( 3 );
    root . left = TreeNode ( 4 );
    root . right = TreeNode ( 5 );
    root . left . left = TreeNode ( 1 );
    root . left . right = TreeNode ( 2 );
    subRoot = TreeNode ( 4 );
    subRoot . left = TreeNode ( 1 );
    subRoot . var right = TreeNode ( 2 );
    var out = sObj . isSubtree ( root , subRoot );
    System.out.println ( out );
}
 