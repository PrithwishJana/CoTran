var n = int ( input ( ) );
var sushi = { int ( x ) for x in input ( ) . split ( ) };
var res = 0;
before , after = 0 , 0;
cur = sushi { 0 };
i = 0;
while (i < n) {
    if (sushi { i } == cur) {
        before += 1;
        i += 1;
    }
     else{
        j = i;
        jS = sushi { j };
        cur = sushi { j };
        while (j < n and sushi { j } == jS) {
            after += 1;
            j += 1;
        }
         i = j;
        res = max ( res , min ( before , after ) );
        var before = after;
        var after = 0;
    }
}
 System.out.println ( res * 2 );
