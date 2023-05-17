var N = int ( input ( ) );
var t = list ( map ( int , input ( ) . split ( ) ) );
v = list ( map ( int , input ( ) . split ( ) ) );
time = 0;
sum_t = sum ( t );
velo_cap = { float ( "inf" ) } * ( 2 * sum_t + 1 );
for i in range ( N ) :
    start_t = time;
    goal_t = time + 2 * t { i };
    for s in range ( 0 , 2 * sum_t + 1 ) :
        if (s < start_t) {
            velo_cap { s } = min ( velo_cap { s } , 2 * v { i } + ( start_t - s ) );
        }
         else if (s < goal_t){
            velo_cap { s } = min ( velo_cap { s } , 2 * v { i } );
        }
        else{
            velo_cap { s } = min ( velo_cap { s } , 2 * v { i } + ( s - goal_t ) );
        }
    time += 2 * t { i };
for s in range ( 2 * sum_t + 1 ) :
    velo_cap { s } = min ( velo_cap { s } , 2 * sum_t - s , s );
System.out.println ( sum ( velo_cap ) / 4 - ( velo_cap { 0 } + velo_cap { - 1 } ) / 8 );
