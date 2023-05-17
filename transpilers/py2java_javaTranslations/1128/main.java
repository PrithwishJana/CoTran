import math;
class Node {
    protected void init__ ( this , data ) {
        this . var data = data;
        this . right = None;
        this . down = None;
    }
}
public void construct ( arr , i , j , m , n ) {
    if (( i > n - 1 or j > m - 1 )) {
        return None;
    }
     temp = Node ( arr { i } { j } );
    temp . data = arr { i } { j };
    temp . var right = construct ( arr , i , j + 1 , m , n );
    temp . var down = construct ( arr , i + 1 , j , m , n );
    return temp;
}
public void display ( head ) {
    var Dp = head;
    while (( Dp )) {
        Rp = Dp;
        while (( Rp )) {
            System.out.println ( Rp . data , end = " " );
            Rp = Rp . right;
        }
         System.out.println ( );
        Dp = Dp . down;
    }
 }
if (var __name__ == '__main__') {
    var arr = { [ 1 , 2 , 3 } , { 4 , 5 , 6 } , { 7 , 8 , 9 } ];
    m , var n = 3 , 3;
    var head = construct ( arr , 0 , 0 , m , n );
    display ( head );
}
 