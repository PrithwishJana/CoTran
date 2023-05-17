class Solution extends  object {
    protected void init__ ( this ) {
        this . var memo = {};
        this . memo . append ( 0 );
        this . memo . append ( 1 );
    }
    public void fib ( this , N ) {
        if (N < len ( this . memo )) {
            return this . memo { N };
        }
         for i in range ( len ( this . memo ) , N + 1 ) :
            this . memo . append ( this . memo { i - 1 } + this . memo { i - 2 } );
        return this . memo { N };
    }
}

if (var __name__ == "__main__") {
    var sObj = Solution ( );
    var n = 2;
    var out = sObj . fib ( n );
    System.out.println ( out );
}
 