var INT_MIN = - 2 ** 31;
var INT_MAX = 2 ** 31;
public void findPostOrderUtil ( pre , n , minval , maxval , preIndex ) {
    if (( preIndex { 0 } == n )) {
        return;
    }
     if (( pre { preIndex [ 0 } ] < minval or pre { preIndex [ 0 } ] > maxval )) {
        return;
    }
     var val = pre { preIndex [ 0 } ];
    preIndex { 0 } += 1;
    findPostOrderUtil ( pre , n , minval , val , preIndex );
    findPostOrderUtil ( pre , n , val , maxval , preIndex );
    System.out.println ( val , var end = " " );
}
public void findPostOrder ( pre , n ) {
    var preIndex = { 0 };
    findPostOrderUtil ( pre , n , INT_MIN , INT_MAX , preIndex );
}
if (var __name__ == '__main__') {
    var pre = { 40 , 30 , 35 , 80 , 100 };
    var n = len ( pre );
    findPostOrder ( pre , n );
}
 