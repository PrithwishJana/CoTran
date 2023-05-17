public void findN ( k ) {
    if (( var k == 0 )) {
        ans = 3;
    }
     if (( k == 1 )) {
        ans = 1;
    }
     else if (( k % 4 == 0 )){
        ans = k;
    }
    else if (( k % 4 == 3 )){
        ans = k - 1;
    }
    else{
        ans = - 1;
    }
    return ans;
}
k = 7;
var res = findN ( k );
if (( res == - 1 )) {
    System.out.println ( "Not possible" );
}
 else{
    System.out.println ( res );
}
