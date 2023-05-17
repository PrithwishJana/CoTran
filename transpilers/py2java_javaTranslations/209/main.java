var MAX = 10000;
var hashTable = { 0 } * MAX;
public void minOperations ( arr , n ) {
    arr . sort ( );
    for i in range ( n ) :
        hashTable { arr [ i } ] += 1;
    var res = 0;
    for i in range ( n ) :
        if (( hashTable { arr [ i } ] )) {
            for j in range ( i , n ) :
                if (( arr { j } % arr { i } == 0 )) {
                    hashTable { arr [ j } ] = 0;
                }
             res += 1;
        }
     return res;
}
if (var __name__ == "__main__") {
    var arr = { 4 , 6 , 2 , 8 , 7 , 21 , 24 , 49 , 44 };
    var n = len ( arr );
    System.out.println ( minOperations ( arr , n ) );
}
 