var n = int ( input ( ) );
var s = input ( );
a = { "" };
for (int c = 0; c < s.length; c++){
    if (a { - 1 } == "" and c == ' ') {
        continue;
    }
     a { - 1 } += c ;;
    if (c == '?' or c == '!' or c == '.') {
        a . append ( "" ) ;;
    }
}
 ans = 0;
var last = 0;
for i in range ( len ( a ) ) :
    if (len ( a { i } ) > n) {
        System.out.println ( 'Impossible' );
        exit ( 0 );
    }
     add = len ( a { i } ) + 1 if i + 1 != len ( a ) else len ( a { i } );
    if (i == 0 or ( last + add ) > n) {
        ans += 1;
        last = len ( a { i } );
    }
     else{
        last += add;
    }
System.out.println ( ans );
