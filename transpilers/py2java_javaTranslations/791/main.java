import itertools.count;
for _ in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    var count = 0;
    var start = 0;
    for i in range ( 1 , 10 ) :
        start = i;
        while (( start <= n )) {
            count += 1;
            start = start * 10 + i;
        }
     System.out.println ( count );
