import glob, imp, inspect, os
import BasicCli, CliParser

DEFAULT_DOC = "CLI utility extension %s"

tokenUtility = CliParser.KeywordRule( "utility",
                                      "CLI utility extensions" )

stringRule = CliParser.StringRule( name="string",
                                   helpname="string",
                                   helpdesc="String" )

argumentRule = CliParser.OptionalRule( stringRule,
                                       "",
                                       name="argument" )

for path in glob.glob( os.path.join( os.path.dirname(__file__),
                                     "Utility",
                                     "*.py" ) ):
    file = os.path.basename( path )

    if file == "__init__.py":
        continue

    name = os.path.splitext( file )[0]

    try:
        module = imp.load_source( name, path )
    except ImportError:
        continue

    for name, object in inspect.getmembers( module,
                                            lambda object: inspect.isclass( object ) or
                                                           inspect.isfunction( object ) ):
        name = name.lower()

        if inspect.isclass( object ):
            doc = DEFAULT_DOC % name
            if object.__doc__ is not None:
                doc = object.__doc__.strip()
            tokenClass = CliParser.KeywordRule( name, doc )

            instance = object()
            if hasattr( instance, "__call__" ):
                BasicCli.registerShowCommand ( tokenUtility,
                                               tokenClass,
                                               argumentRule,
                                               instance )
            else:
                for name, object in inspect.getmembers( instance,
                                                        inspect.ismethod ):

            	    doc = DEFAULT_DOC % name
            	    if object.__doc__ is not None:
                	doc = object.__doc__.strip()
                    tokenFunction = CliParser.KeywordRule( name, doc )

                    BasicCli.registerShowCommand ( tokenUtility,
                                                   tokenClass,
                                                   tokenFunction,
                                                   argumentRule,
                                                   object )
        elif inspect.isfunction( object ):
            doc = DEFAULT_DOC % name
            if object.__doc__ is not None:
                doc = object.__doc__.strip()
            tokenFunction = CliParser.KeywordRule( name, doc )

            BasicCli.registerShowCommand ( tokenUtility,
                                           tokenFunction,
                                           argumentRule,
                                           object )
