h , var w = map ( int , input ( ) . split ( ) );
var s = { list ( input ( ) ) for _ in range ( h ) };
ans = 0;
var ci = { 0 for _ in range ( w ) };
for i in range ( h - 1 , - 1 , - 1 ) :
    var co = 0;
    for j in range ( w - 1 , - 1 , - 1 ) :
        if (s { i } { j } == 'J') {
            ans += co * ci { j };
        }
         else if (s { i } { j } == 'O'){
            co += 1;
        }
        else if (s { i } { j } == 'I'){
            ci { j } += 1;
        }
System.out.println ( ans );
