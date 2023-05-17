public void NthCharacter ( n ) {
    var s = "";
    var c = 1;
    while (( true )) {
        if (( c < 10 )) {
            s += chr ( 48 + c );
        }
         else{
            var s1 = "";
            dup = c;
            while (( dup > 0 )) {
                s1 += chr ( ( dup % 10 ) + 48 );
                dup //= 10;
            }
             s1 = "" . join ( reversed ( s1 ) );
            s += s1;
        }
        c += 1;
        if (( len ( s ) >= n )) {
            return s { n - 1 };
        }
     }
 }
if (var __name__ == "__main__") {
    var n = 11;
    System.out.println ( NthCharacter ( n ) );
}
 