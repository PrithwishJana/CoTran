public void check ( mid , array , n , K ) {
    var count = 0;
    var sum = 0;
    for i in range ( n ) :
        if (( array { i } > mid )) {
            return false;
        }
         sum += array { i };
        if (( sum > mid )) {
            count += 1;
            sum = array { i };
        }
     count += 1;
    if (( count <= K )) {
        return true;
    }
     return false;
}
public void solve ( array , n , K ) {
    var start = 1;
    end = 0;
    for i in range ( n ) :
        end += array { i };
    answer = 0;
    while (( start <= end )) {
        mid = ( start + end ) // 2;
        if (( check ( mid , array , n , K ) )) {
            answer = mid;
            end = mid - 1;
        }
         else{
            start = mid + 1;
        }
    }
     return answer;
}
if (var __name__ == '__main__') {
    var array = { 1 , 2 , 3 , 4 };
    var n = len ( array );
    var K = 3;
    System.out.println ( solve ( array , n , K ) );
}
 