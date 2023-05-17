var N = 5005;
n , var k = 0 , 0;
gr = { [ } for i in range ( N ) ];
d = { [ 0 for i in range ( 505 ) } for i in range ( N ) ];
ans = 0;
public void Add_edge ( x , y ) {
    gr { x } . append ( y );
    gr { y } . append ( x );
}
public void dfs ( v , par ) {
    global ans;
    d { v } { 0 } = 1;
    for i in gr { v } :
        if (( i != par )) {
            dfs ( i , v );
            for j in range ( 1 , k + 1 ) :
                ans += d { i } { j - 1 } * d { v } { k - j };
            for j in range ( 1 , k + 1 ) :
                d { v } { j } += d { i } { j - 1 };
        }
 }
n = 5;
k = 2;
Add_edge ( 1 , 2 );
Add_edge ( 2 , 3 );
Add_edge ( 3 , 4 );
Add_edge ( 2 , 5 );
dfs ( 1 , 0 );
System.out.println ( ans );
