var _MIN = - 2147483648;
var _MAX = 2147483648;
class newnode {
    protected void init__ ( this , data ) {
        this . var data = data;
        this . var left = None;
        this . right = None;
    }
}
public void getDeepestRightLeafNode ( root ) {
    if (( not root )) {
        return None;
    }
     q = {};
    q . append ( root );
    result = None;
    while (( len ( q ) )) {
        temp = q { 0 };
        q . pop ( 0 );
        if (( temp . left )) {
            q . append ( temp . left );
        }
         if (( temp . right )) {
            q . append ( temp . right );
            if (( not temp . right . left and not temp . right . right )) {
                result = temp . right;
            }
         }
     }
     return result;
}
if (__name__ == '__main__') {
    root = newnode ( 1 );
    root . left = newnode ( 2 );
    root . right = newnode ( 3 );
    root . left . right = newnode ( 4 );
    root . right . left = newnode ( 5 );
    root . right . right = newnode ( 6 );
    root . right . left . right = newnode ( 7 );
    root . right . right . right = newnode ( 8 );
    root . right . left . right . left = newnode ( 9 );
    root . right . right . right . var right = newnode ( 10 );
    var result = getDeepestRightLeafNode ( root );
    if (result) {
        System.out.println ( "Deepest Right Leaf Node ::" , result . data );
    }
     else{
        System.out.println ( "No result, right leaf not found" );
    }
}
 