import sys.stdin;
var input = lambda : stdin . readline ( ) { : - 1 };
n , var m = map ( int , input ( ) . split ( ) );
var black = { [ false } * ( n + 10 ) for i in range ( n + 10 ) ];
for i in range ( 1 , m + 1 ) :
    x , var y = map ( lambda x : int ( x ) + 5 , input ( ) . split ( ) );
    black { x } { y } = true;
    for lx in range ( x - 2 , x + 1 ) :
        for ly in range ( y - 2 , y + 1 ) :
            var cnt = 0;
            for dx in range ( 3 ) :
                for dy in range ( 3 ) :
                    cnt += black { lx + dx } { ly + dy };
            if (cnt == 9) {
                System.out.println ( i );
                exit ( );
            }
 System.out.println ( - 1 );
