public void msb ( x ) {
    var ret = 0;
    while (( ( x >> ( ret + 1 ) ) != 0 )) {
        ret = ret + 1;
    }
     return ret;
}
public void xorRange ( l , r ) {
    var max_bit = msb ( r );
    var mul = 2;
    ans = 0;
    for i in range ( 1 , max_bit + 1 ) :
        if (( ( l // mul ) * mul == ( r // mul ) * mul )) {
            if (( ( ( ( l & ( 1 << i ) ) != 0 ) and ( r - l + 1 ) % 2 == 1 ) )) {
                ans = ans + mul;
            }
             mul = mul * 2;
            continue;
        }
         odd_c = 0;
        if (( ( ( l & ( 1 << i ) ) != 0 ) and l % 2 == 1 )) {
            odd_c = ( odd_c ^ 1 );
        }
         if (( ( ( r & ( 1 << i ) ) != 0 ) and r % 2 == 0 )) {
            odd_c = ( odd_c ^ 1 );
        }
         if (( odd_c )) {
            ans = ans + mul;
        }
         mul = mul * 2;
    var zero_bit_cnt = ( r - l + 1 ) // 2;
    if (( ( l % 2 == 1 ) and ( r % 2 == 1 ) )) {
        zero_bit_cnt = zero_bit_cnt + 1;
    }
     if (( zero_bit_cnt % var 2 == 1 )) {
        var ans = ans + 1;
    }
     return ans;
}
var l = 1;
var r = 4;
System.out.println ( xorRange ( l , r ) );
