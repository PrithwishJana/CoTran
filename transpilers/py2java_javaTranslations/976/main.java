var CHARS = 26;
public void isValidString ( str ) {
    var freq = { 0 } * CHARS;
    for i in range ( len ( str ) ) :
        freq { ord ( str [ i } ) - ord ( 'a' ) ] += 1;
    var freq1 = 0;
    count_freq1 = 0;
    for i in range ( CHARS ) :
        if (( freq { i } != 0 )) {
            freq1 = freq { i };
            count_freq1 = 1;
            break;
        }
     var freq2 = 0;
    count_freq2 = 0;
    for j in range ( i + 1 , CHARS ) :
        if (( freq { j } != 0 )) {
            if (( freq { j } == freq1 )) {
                count_freq1 += 1;
            }
             else{
                count_freq2 = 1;
                freq2 = freq { j };
                break;
            }
        }
     for k in range ( j + 1 , CHARS ) :
        if (( freq { k } != 0 )) {
            if (( freq { k } == freq1 )) {
                count_freq1 += 1;
            }
             if (( freq { k } == freq2 )) {
                count_freq2 += 1;
            }
             else{
                return false;
            }
        }
         if (( count_freq1 > 1 and count_freq2 > 1 )) {
            return false;
        }
     return true;
}
if (var __name__ == "__main__") {
    var str = "abcbc";
    if (( isValidString ( str ) )) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
}
 