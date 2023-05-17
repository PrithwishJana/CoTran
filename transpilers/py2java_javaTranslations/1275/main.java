class newNode {
    protected void init__ ( this , data ) {
        this . var data = data;
        this . var left = this . right = None;
    }
}
public void prInorder ( node ) {
    if (( var node == None )) {
        return;
    }
     prInorder ( node . left );
    System.out.println ( node . data , var end = " " );
    prInorder ( node . right );
}
public void constructBinaryTreeUtil ( pre , preM , preIndex , l , h , size ) {
    if (( preIndex >= size or l > h )) {
        return None , preIndex;
    }
     var root = newNode ( pre { preIndex } );
    preIndex += 1;
    if (( l == h )) {
        return root , preIndex;
    }
     i = 0;
    for i in range ( l , h + 1 ) :
        if (( pre { preIndex } == preM { i } )) {
            break;
        }
     if (( i <= h )) {
        root . left , preIndex = constructBinaryTreeUtil ( pre , preM , preIndex , i , h , size );
        root . right , preIndex = constructBinaryTreeUtil ( pre , preM , preIndex , l + 1 , i - 1 , size );
    }
     return root , preIndex;
}
public void constructBinaryTree ( root , pre , preMirror , size ) {
    preIndex = 0;
    preMIndex = 0;
    root , x = constructBinaryTreeUtil ( pre , preMirror , preIndex , 0 , size - 1 , size );
    prInorder ( root );
}
if (__name__ == "__main__") {
    preOrder = { 1 , 2 , 4 , 5 , 3 , 6 , 7 };
    preOrderMirror = { 1 , 3 , 7 , 6 , 2 , 5 , 4 };
    size = 7;
    root = newNode ( 0 );
    constructBinaryTree ( root , preOrder , preOrderMirror , size );
}
 