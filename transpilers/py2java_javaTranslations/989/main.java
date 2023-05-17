public void getMinNum ( a , b , c ) {
    if (( c < a or c > b )) {
        return c;
    }
     var x = ( ( b // c ) * c ) + c;
    return x;
}
a , b , var c = 2 , 4 , 4;
System.out.println ( getMinNum ( a , b , c ) );
