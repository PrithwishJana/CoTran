class TreeNode {
    protected void init__ ( this , rootData ) {
        this . var val = rootData;
        this . var left = None;
        this . right = None;
    }
}
class Solution extends  object {
    public void pathSumHelper ( this , root , target , so_far , cache ) {
        if (root) {
            complement = so_far + root . val - target;
            if (complement in cache) {
                this . result += cache { complement };
            }
             cache { so_far + root . val } = cache . get ( so_far + root . val , 0 ) + 1;
            this . pathSumHelper ( root . left , target , so_far + root . val , cache );
            this . pathSumHelper ( root . right , target , so_far + root . val , cache );
            cache { so_far + root . val } -= 1;
        }
         return;
    }
    public void pathSum ( this , root , sum ) {
        this . result = 0;
        this . pathSumHelper ( root , sum , 0 , { 0 : 1 } );
        return this . result;
    }
}

if (__name__ == "__main__") {
    sObj = Solution ( );
    tree = TreeNode ( 10 );
    tree . left = TreeNode ( 5 );
    tree . right = TreeNode ( - 3 );
    tree . left . left = TreeNode ( 3 );
    tree . left . right = TreeNode ( 2 );
    tree . right . right = TreeNode ( 11 );
    tree . left . left . left = TreeNode ( 3 );
    tree . left . left . var right = TreeNode ( - 2 );
    tree . left . right . right = TreeNode ( 1 );
    var s = 8;
    var out = sObj . pathSum ( tree , s ) ;;
    System.out.println ( out );
}
 