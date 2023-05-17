import math.gcd as __gcd;
public void finalNum ( arr , n ) {
    var result = arr { 0 };
    for (int i = 0; i < arr.length; i++){
        result = __gcd ( result , i );
    }
    return result;
}
var arr = { 3 , 9 , 6 , 36 };
var n = len ( arr );
System.out.println ( finalNum ( arr , n ) );
