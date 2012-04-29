class Firewall( object ):
    """Foo bar baz"""

    def __init__( self ):
        self._state = ""

    def __call__( self, device, argument ):
        print "%s -> firewall -> %s" % (self._state, argument)
        self._state = argument
