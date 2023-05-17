import itertools;
public void findNth ( n ) {
    var count = 0;
    for curr in itertools . count ( ) :
        sum = 0;
        x = curr;
        while (( x )) {
            sum = sum + x % 10;
            x = x // 10;
        }
         if (( sum == 10 )) {
            count = count + 1;
         }
         if (( count == n )) {
            return curr;
        }
     return - 1;
}
if (var __name__ == '__main__') {
    System.out.println ( findNth ( 5 ) );
}
 