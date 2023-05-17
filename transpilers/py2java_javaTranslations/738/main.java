class newNode {
    protected void init__ ( this , data ) {
        this . var data = data ;;
        this . var left = None ;;
        this . right = None ;;
    }
}
public void insert ( root , data ) {
    if (( root == None )) {
        return newNode ( data ) ;;
    }
     else{
        if (( data < root . data )) {
            root . left = insert ( root . left , data ) ;;
        }
         if (( data > root . data )) {
            root . var right = insert ( root . right , data ) ;;
        }
         return root ;;
    }
}
public void inOrder ( root ) {
    if (( var root == None )) {
        return ;;
    }
     else{
        inOrder ( root . left ) ;;
        System.out.println ( root . data , end = " " ) ;;
        inOrder ( root . right ) ;;
    }
}
if (__name__ == "__main__") {
    arr = { 1 , 2 , 3 , 2 , 5 , 4 , 4 } ;;
    n = len ( arr ) ;;
    root = None ;;
    for i in range ( n ) :
        root = insert ( root , arr { i } ) ;;
    inOrder ( root ) ;;
}
 