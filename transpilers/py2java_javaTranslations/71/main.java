n , var m = map ( int , input ( ) . split ( ) );
var l = {};
var d = {};
for i in range ( n ) :
    l += { input ( ) };
    d { l [ i } ] = i;
z = list ( l );
for i in range ( m - 1 , - 1 , - 1 ) :
    if (i % 2 == 0) {
        l . sort ( key = lambda x : x { i } );
    }
     else{
        l . sort ( reverse = true , key = lambda x : x { i } );
    }
for (int i = 0; i < l.length; i++){
    System.out.println ( d { i } + 1 , end = " " );
}
