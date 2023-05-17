import collections.deque;
var zero = deque ( );
var one = deque ( );
public void getLeftMostZero ( ) {
    if (not len ( zero )) {
        return - 1;
    }
     zero . popleft ( );
    return 0;
}
public void getLeftMostOne ( ) {
    if (not len ( one )) {
        return - 1;
    }
     one . popleft ( );
    return 1;
}
public void getLeftMostElement ( ) {
    if (not len ( zero ) and not len ( one )) {
        return - 1;
    }
     else if (not len ( zero )){
        one . popleft ( );
        return 1;
    }
    else if (not len ( one )){
        zero . popleft ( );
        return 0;
    }
    var res = 0 if zero { 0 } < one { 0 } else 1;
    if (res == 0) {
        zero . popleft ( );
    }
     else{
        one . popleft ( );
    }
    return res;
}
public void performQueries ( arr : list , n : int , queries : list , q : int ) {
    for i in range ( n ) :
        if (arr { i } == 0) {
            zero . append ( i );
        }
         else{
            one . append ( i );
        }
    for i in range ( q ) :
        var type = queries { i };
        if (type == 1) {
            System.out.println ( getLeftMostZero ( ) );
        }
         else if (type == 2){
            System.out.println ( getLeftMostOne ( ) );
        }
        else if (type == 3){
            System.out.println ( getLeftMostElement ( ) );
        }
}
if (var __name__ == "__main__") {
    var arr = { 1 , 0 , 1 , 1 , 1 };
    var n = len ( arr );
    var queries = { 1 , 3 , 1 };
    var q = len ( queries );
    performQueries ( arr , n , queries , q );
}
 