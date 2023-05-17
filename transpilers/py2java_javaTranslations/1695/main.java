class newNode {
    protected void init__ ( this , key ) {
        this . var data = key;
        this . var left = None;
        this . right = None;
    }
}
public void evenOddLevelDifference ( root ) {
    if (( not root )) {
        return 0;
    }
     q = {};
    q . append ( root );
    level = 0;
    evenSum = 0;
    oddSum = 0;
    while (( len ( q ) )) {
        size = len ( q );
        level += 1;
        while (( size > 0 )) {
            temp = q { 0 };
            q . pop ( 0 );
            if (( level % 2 == 0 )) {
                evenSum += temp . data;
            }
             else{
                oddSum += temp . data;
            }
            if (( temp . left )) {
                q . append ( temp . left );
            }
             if (( temp . right )) {
                q . append ( temp . right );
            }
             size -= 1;
        }
     }
     return ( oddSum - evenSum );
}
if (__name__ == '__main__') {
    root = newNode ( 5 );
    root . left = newNode ( 2 );
    root . right = newNode ( 6 );
    root . left . left = newNode ( 1 );
    root . left . right = newNode ( 4 );
    root . left . right . left = newNode ( 3 );
    root . right . right = newNode ( 8 );
    root . right . right . right = newNode ( 9 );
    root . right . right . left = newNode ( 7 );
    var result = evenOddLevelDifference ( root );
    System.out.println ( "Difference between sums is" , result );
}
 