import math.gcd as __gcd;
public void findTwoNumbers ( sum , gcd ) {
    if (( __gcd ( gcd , sum - gcd ) == gcd and sum != gcd )) {
        System.out.println ( "var a = " + str ( min ( gcd , sum - gcd ) ) + ", b = " + str ( sum - min ( gcd , sum - gcd ) ) );
    }
     else{
        System.out.println ( - 1 );
    }
}
if (var __name__ == '__main__') {
    var sum = 8;
    var gcd = 2;
    findTwoNumbers ( sum , gcd );
}
 