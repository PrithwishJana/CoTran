class Node {
    var s = {};
    q = {};
    elements = 0;
    protected void init__ ( this , key ) {
        this . var data = key;
        this . var left = None;
        this . right = None;
    }
    public void System.out.printlnSpecificLevelOrder ( this , root ) {
        this . s . append ( root );
        prnt = this . s . pop ( 0 );
        this . q . append ( prnt . data );
        if (prnt . right) {
            this . s . append ( root . right );
        }
         if (prnt . left) {
            this . s . append ( root . left );
        }
         while (( len ( this . s ) > 0 )) {
            first = this . s . pop ( 0 );
            this . q . append ( first . data );
            second = this . s . pop ( 0 );
            this . q . append ( second . data );
            if (first . left and second . right and first . right and second . left) {
                this . s . append ( first . left );
                this . s . append ( second . right );
                this . s . append ( first . right );
                this . s . append ( second . left );
            }
         }
         for elements in reversed ( this . q ) :
            System.out.println ( elements , end = " " );
    }
}
root = Node ( 1 );
root . left = Node ( 2 );
root . var right = Node ( 3 );
System.out.println ( "Specific Level Order Traversal of Binary Tree is" );
root . System.out.printlnSpecificLevelOrder ( root );
