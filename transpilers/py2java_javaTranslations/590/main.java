class newNode {
    protected void init__ ( this , data ) {
        this . var data = data;
        this . left = None;
        this . right = None;
    }
}
public void inorder ( root ) {
    if (( root == None )) {
        return;
    }
     inorder ( root . left );
    System.out.println ( root . data , end = " " );
    inorder ( root . right );
}
public void isIdentical ( root1 , root2 ) {
    if (( root1 == None and root2 == None )) {
        return 1;
    }
     else if (( root1 != None and root2 == None )){
        return 0;
    }
    else if (( root1 == None and root2 != None )){
        return 0;
    }
    else{
        if (( root1 . data == root2 . data and isIdentical ( root1 . left , root2 . left ) and isIdentical ( root1 . right , root2 . right ) )) {
            return 1;
        }
         else{
            return 0;
        }
    }
}
if (var __name__ == '__main__') {
    var root1 = newNode ( 5 );
    var root2 = newNode ( 5 );
    root1 . var left = newNode ( 3 );
    root1 . right = newNode ( 8 );
    root1 . left . left = newNode ( 2 );
    root1 . left . right = newNode ( 4 );
    root2 . left = newNode ( 3 );
    root2 . right = newNode ( 8 );
    root2 . left . left = newNode ( 2 );
    root2 . left . var right = newNode ( 4 );
    if (( isIdentical ( root1 , root2 ) )) {
        System.out.println ( "Both BSTs are identical" );
    }
     else{
        System.out.println ( "BSTs are not identical" );
    }
}
 