public void fun ( n ) {
    return n & ( n - 1 );
}
var n = 7;
System.out.println ( "The number after unsetting the rightmost set bit" , fun ( n ) );
