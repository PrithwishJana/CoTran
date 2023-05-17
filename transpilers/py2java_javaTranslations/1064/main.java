def _input ( ) : return map ( int , input ( ) . split ( ) );
n , var m = _input ( );
var lst = list ( _input ( ) );
var l = {};
for i in range ( n ) :
    if (lst { i } not in l) {
        l { lst [ i } ] = 1;
    }
     else : l { lst [ i } ] += 1;
var res = 0;
for i in range ( n ) :
    if (l { lst [ i } ] > 1) {
        res += n - i - l { lst [ i } ];
        l { lst [ i } ] -= 1;
    }
     else{
        res += n - i - 1;
    }
System.out.println ( res );
