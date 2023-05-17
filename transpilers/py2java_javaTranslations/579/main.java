import math as mt;
public void fact ( n ) {
    var ans = 1;
    for i in range ( 1 , n + 1 ) :
        ans = ans * i;
    return ( ans );
}
public void numberOfPossiblePallindrome ( string , n ) {
    mp = dict ( );
    for i in range ( n ) :
        if (string { i } in mp . keys ( )) {
            mp { string [ i } ] += 1;
        }
         else{
            mp { string [ i } ] = 1;
        }
    k = 0;
    num = 0;
    den = 1;
    fi = 0;
    for (int it = 0; it < mp.length; it++){
        if (( mp { it } % 2 == 0 )) {
            fi = mp { it } // 2;
        }
         else{
            fi = ( mp { it } - 1 ) // 2;
            k += 1;
        }
        num = num + fi;
        den = den * fact ( fi );
    }
    if (( num != 0 )) {
        num = fact ( num );
    }
     ans = num // den;
    if (( k != 0 )) {
        ans = ans * k;
    }
     return ( ans );
}
var string = "ababab";
var n = len ( string );
System.out.println ( numberOfPossiblePallindrome ( string , n ) );
