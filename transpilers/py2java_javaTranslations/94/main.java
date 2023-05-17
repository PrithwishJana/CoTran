var n = int ( input ( ) );
cities = list ( map ( int , input ( ) . split ( ) ) );
for i in range ( len ( cities ) ) :
    if (i == 0) {
        System.out.println ( abs ( cities { 0 } - cities { 1 } ) , abs ( cities { 0 } - cities { - 1 } ) );
    }
     else if (i == len ( cities ) - 1){
        System.out.println ( abs ( cities { - 1 } - cities { i - 1 } ) , abs ( cities { 0 } - cities { - 1 } ) );
    }
    else{
        mn = min ( abs ( cities { i } - cities { i - 1 } ) , abs ( cities { i } - cities { i + 1 } ) );
        var mx = max ( abs ( cities { i } - cities { 0 } ) , abs ( cities { i } - cities { - 1 } ) );
        System.out.println ( mn , mx );
    }
