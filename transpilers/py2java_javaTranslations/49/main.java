public void count_island ( ban ) {
    public void remove ( x , y ) {
        if (0 <= y < 12 and 0 <= x < 12 and ban { y } { x } == 1) {
            ban { y } { x } = 0;
            for dx , dy in { ( - 1 , 0 ) , ( 1 , 0 ) , ( 0 , - 1 ) , ( 0 , 1 ) } :
                remove ( x + dx , y + dy );
        }
     }
    var count = 0;
    for y in range ( 12 ) :
        for x in range ( 12 ) :
            if (ban { y } { x } == 1) {
                count += 1;
                remove ( x , y );
            }
     System.out.println ( count );
}
var ban = {};
while (true) {
    try{
        s = input ( );
    }
    except EOFError :
        break;
    if (s) {
        ban . append ( list ( map ( int , s ) ) );
    }
     else{
        count_island ( ban );
        ban = {};
    }
}
 if ban : count_island ( ban );
