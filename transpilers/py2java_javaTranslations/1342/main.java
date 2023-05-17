public void getModulo ( n , d ) {
    return ( n & ( d - 1 ) );
}
var n = 6;
var d = 4;
System.out.println ( n , "moduo" , d , "is" , getModulo ( n , d ) );
