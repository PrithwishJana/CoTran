public void findPerm ( n , differences ) {
    var ans = {};
    ans . append ( 0 );
    x = 0;
    for i in range ( n - 1 ) :
        diff = differences { i };
        x = x + diff;
        ans . append ( x );
    anss = ans;
    ans = sorted ( ans );
    var flag = - 1;
    for i in range ( 1 , n ) :
        res = ans { i } - ans { i - 1 };
        if (( res != 1 )) {
            flag = 0;
        }
     if (( flag == 0 )) {
        System.out.println ( "-1" );
        return;
    }
     else{
        var mpp = dict ( );
        var j = 1;
        var value_at_index = {};
        for (int x = 0; x < ans.length; x++){
            mpp { x } = j;
            j += 1;
        }
        for (int x = 0; x < anss.length; x++){
            value_at_index . append ( mpp { x } );
        }
        for (int x = 0; x < value_at_index.length; x++){
            System.out.println ( x , var end = " " );
        }
        System.out.println ( );
    }
}
var differences = {};
differences . append ( 2 );
differences . append ( - 3 );
differences . append ( 2 );
var n = len ( differences ) + 1;
findPerm ( n , differences );
