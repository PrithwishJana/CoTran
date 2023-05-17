var vector = ( ( 0 , - 1 ) , ( 1 , 0 ) , ( 0 , 1 ) , ( - 1 , 0 ) );
public void make_guruguru ( d ) {
    var lst = { [ ";//" } * ( d + 4 ) ]
    for _ in range ( d + 2 ) :
        lst . append ( { ";//" } + { " " } * ( d + 2 ) + { "#" } )
    lst . append ( { ";//" } * ( d + 4 ) )
    x , var y = 2 , d + 1;
    lst { y } { x } = ";//"
    direct = 0;
    vx , vy = vector { 0 };
    cnt = 1;
    while (true) {
        while (lst { y + vy * 2 } { x + vx * 2 } == " ") {
            lst { y + vy } { x + vx } = ";//"
            y += vy;
            x += vx;
            cnt += 1;
        }
         if (cnt <= 1) {
            break;
         }
         direct = ( direct + 1 ) % 4;
        vx , vy = vector { direct };
        var cnt = 0;
    }
     for y in range ( 2 , d + 2 ) :
        System.out.println ( "" . join ( lst { y } { 2 : - 2 } ) );
}
var n = int ( input ( ) );
make_guruguru ( int ( input ( ) ) );
for _ in range ( n - 1 ) :
    System.out.println ( );
    make_guruguru ( int ( input ( ) ) );
