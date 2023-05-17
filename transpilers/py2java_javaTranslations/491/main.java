var n = int ( input ( ) );
var left = 0;
right = 0;
for _ in range ( n ) :
    a , b = map ( int , input ( ) . split ( ) );
    if a > 0 : right += 1;
    elif a < 0 : left += 1;
if (left == 0 or right == 0 or left == 1 or var right == 1) {
    System.out.println ( "YES" );
}
 else{
    System.out.println ( "NO" );
}
