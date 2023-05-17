public void minimumCostOfBreaking ( X , Y , m , n ) {
    var res = 0;
    X . sort ( var reverse = true );
    Y . sort ( reverse = true );
    var hzntl = 1 ; vert = 1;
    var i = 0 ; j = 0;
    while (( i < m and j < n )) {
        if (( X { i } > Y { j } )) {
            res += X { i } * vert;
            hzntl += 1;
            i += 1;
        }
         else{
            res += Y { j } * hzntl;
            vert += 1;
            j += 1;
        }
    }
     var total = 0;
    while (( i < m )) {
        total += X { i };
        i += 1;
    }
     res += total * vert;
    total = 0;
    while (( j < n )) {
        total += Y { j };
        j += 1;
    }
     res += total * hzntl;
    return res;
}
var m = 6 ; n = 4;
var X = { 2 , 1 , 3 , 1 , 4 };
var Y = { 4 , 1 , 2 };
System.out.println ( minimumCostOfBreaking ( X , Y , m - 1 , n - 1 ) );
