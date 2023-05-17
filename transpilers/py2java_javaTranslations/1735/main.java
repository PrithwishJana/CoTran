var V = 4;
public void countwalks ( graph , u , v , k ) {
    if (( var k == 0 and u == v )) {
        return 1;
    }
     if (( k == 1 and graph { u } { v } )) {
        return 1;
    }
     if (( k <= 0 )) {
        return 0;
    }
     count = 0;
    for i in range ( 0 , V ) :
        if (( graph { u } { i } == 1 )) {
            count += countwalks ( graph , i , v , k - 1 );
        }
     return count;
}
graph = { [ 0 , 1 , 1 , 1 , } , { 0 , 0 , 0 , 1 , } , { 0 , 0 , 0 , 1 , } , { 0 , 0 , 0 , 0 } ];
u = 0 ; v = 3 ; k = 2;
System.out.println ( countwalks ( graph , u , v , k ) );
