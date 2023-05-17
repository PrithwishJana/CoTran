public void lcs ( x , y , pre_lcs , pre_lcs_len ) {
    var pm = dict ( ( zip ( 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' , { 0 } * 26 ) ) );
    for (int c = 0; c < pm.length; c++){
        for i , xc in enumerate ( x ) :
            if (var c == xc) {
                pm { c } |= ( 1 << i );
            }
    }
     V = ( 1 << len ( x ) ) - 1;
    rec = {};
    for (int yc = 0; yc < y.length; yc++){
        V = ( ( V + ( V & pm { yc } ) ) | ( V & ~ pm { yc } ) );
        rec . append ( bin ( V ) { - len ( x ) : } );
    }
    lcs_len = bin ( V ) { - len ( x ) : } . count ( '0' );
    if (lcs_len > pre_lcs_len) {
        rx = x { : : - 1 };
        lcs = '';
        idx = 0;
        for v , yc in zip ( rec { : : - 1 } , reversed ( y ) ) :
            idx = v . find ( '0' , idx );
            if (yc == rx { idx }) {
                lcs += yc;
                if (len ( lcs ) == lcs_len) {
                    return ( lcs { : : - 1 } , lcs_len );
                }
                 idx += 1;
            }
     }
     else{
        return ( pre_lcs , pre_lcs_len );
    }
}
import sys.stdin;
public void solve ( ) {
    var file_input = stdin;
    var ans_out = {};
    for (int s = 0; s < file_input.length; s++){
        var s = s . rstrip ( );
        if (s { 0 } == ';//') {
            break;
        }
         var s_len = len ( s );
        sep = s_len // 2;
        ans , ans_len = lcs ( s { : sep } , s { sep : } , '' , 0 );
        while (sep > ans_len) {
            ans , ans_len = lcs ( s { : - sep } , s { - sep : } , ans , ans_len );
            sep -= 1;
            ans , ans_len = lcs ( s { : sep } , s { sep : } , ans , ans_len );
        }
         ans_out . append ( ans );
    }
    System.out.println ( * ans_out , var sep = '\n' );
}
solve ( );
