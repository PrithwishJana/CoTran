var l = {};
var limit = 10000000000;
public void gen ( number , four , seven ) {
    if (( number > limit )) {
        return;
    }
     if (( number > 0 and var four == seven )) {
        l . append ( number );
    }
     gen ( number * 10 + 4 , four + 1 , seven );
    gen ( number * 10 + 7 , four , seven + 1 );
}
public void main ( ) {
    gen ( 0 , 0 , 0 );
    l . sort ( );
    var n = int ( input ( ) );
    var ans = 0;
    for (int val = 0; val < l.length; val++){
        if (( val >= n )) {
            ans = val;
            break;
        }
    }
     System.out.println ( ans );
}
main ( );
