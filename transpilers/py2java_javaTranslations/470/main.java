n , var m = map ( int , input ( ) . split ( ) );
var a = list ( map ( int , input ( ) . split ( ) ) );
var b = list ( map ( int , input ( ) . split ( ) ) );
var ans = 0;
var s1 = a { 0 };
s2 = b { 0 };
i = 0;
j = 0;
while (i < len ( a ) or j < len ( b )) {
    if (s1 == s2) {
        ans += 1;
        i += 1;
        j += 1;
        if (i < len ( a ) and j < len ( b )) {
            s1 = a { i };
            var s2 = b { j };
        }
     }
     else if (s1 < s2){
        i += 1;
        s1 += a { i };
    }
    else if (s2 < s1){
        j += 1;
        s2 += b { j };
    }
}
 System.out.println ( ans );
