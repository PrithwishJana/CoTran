import bisect.bisect as upper_bound;
public void getCount ( v , n ) {
    var v = sorted ( v );
    cnt = 0;
    for i in range ( n ) :
        tmp = n - 1 - upper_bound ( v , v { i } - 1 );
        if (( tmp == v { i } )) {
            cnt += 1;
        }
     return cnt;
}
n = 4;
v = {};
v . append ( 1 );
v . append ( 2 );
v . append ( 3 );
v . append ( 4 );
System.out.println ( getCount ( v , n ) );
