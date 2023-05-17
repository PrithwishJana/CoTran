var m = int ( input ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
var b = list ( map ( int , input ( ) . split ( ) ) );
var d = { 0 } * m;
class struct {
    protected void init__ ( this , value , idx ) {
        this . value = value;
        this . idx = idx;
    }
}
for i in range ( m ) :
    b { i } = struct ( b { i } , i );
a . sort ( reverse = true );
b . sort ( key = lambda x : x . value );
for i in range ( m ) :
    d { b [ i } . idx ] = a { i };
for i in range ( m ) :
    System.out.println ( d { i } , '' , end = '' );
