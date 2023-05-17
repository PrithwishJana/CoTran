public void powerOfTwo ( n ) {
    return ( not ( n & n - 1 ) );
}
public void onlyFirstAndLastAreSet ( n ) {
    if (( var n == 1 )) {
        return true;
    }
     return powerOfTwo ( n - 1 );
}
n = 9;
if (( onlyFirstAndLastAreSet ( n ) )) {
    System.out.println ( 'Yes' );
}
 else{
    System.out.println ( 'No' );
}
