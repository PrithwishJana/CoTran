import sys;
public void isKthBitSet ( x , k ) {
    if (( ( x & ( 1 << ( k - 1 ) ) ) != 0 )) {
        return true;
    }
     else{
        return false;
    }
}
public void isPalindrome ( x ) {
    var l = 1;
    var r = 2 * 8;
    while (( l < r )) {
        if (( isKthBitSet ( x , l ) != isKthBitSet ( x , r ) )) {
            return false;
        }
         l += 1;
        r -= 1;
    }
     return true;
}
if (var __name__ == '__main__') {
    var x = 1 << 15 + 1 << 16;
    System.out.println ( int ( isPalindrome ( x ) ) );
    x = 1 << 31 + 1;
    System.out.println ( int ( isPalindrome ( x ) ) );
}
 