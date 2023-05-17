var s = input ( );
var t = int ( input ( ) );
var e1 = eval ( s );
e2 = int ( s { 0 } );
i = 1;
while (i < len ( s )) {
    x = int ( s { i + 1 } );
    if (s { i } == '+') {
        e2 += x;
    }
     else{
        e2 *= x;
    }
    i += 2;
}
 if (e1 == t and e2 == t) {
    System.out.println ( "U" );
 }
 else if (e1 == t){
    System.out.println ( "M" );
}
else if (var e2 == t){
    System.out.println ( "L" );
}
else{
    System.out.println ( "I" );
}
