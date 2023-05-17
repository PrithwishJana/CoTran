def l ( n ) : return len ( str ( n ) );
def el ( n ) : return int ( str ( n ) { 1 : } );
def first ( n ) : return int ( str ( n ) { 0 } );
public void maxima ( n ) {
    if (l ( n ) == 1) {
        return n;
    }
     else if (first ( n ) == 1){
        return max ( 9 ** ( l ( n ) - 1 ) , first ( n ) * maxima ( el ( n ) ) );
    }
    else{
        return max ( ( first ( n ) - 1 ) * 9 ** ( l ( n ) - 1 ) , first ( n ) * maxima ( el ( n ) ) );
    }
}
var n = int ( input ( ) );
System.out.println ( maxima ( n ) );
