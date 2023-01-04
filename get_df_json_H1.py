import pandas as pd

def get_df_json( json_data, var_name ):

    Xvars_ = (0,1,2)
    varname_ = var_name
    arr_Q2_ = []
    arr_x_ = []
    arr_y_ = []
    arr_val_ = []
    arr_err_ = {}
    
    column_names_ = []
    idx_col_var_ = None
    for idx__,data__ in enumerate( json_data[ 'headers' ] ):
        name__ = data__[ 'name' ]
        if name__ == varname_: idx_col_var_ = idx__
        column_names_.append( data__[ 'name' ] )
    print ( column_names_ )
    
    nXvars_ = None
    for data__ in json_data[ 'values' ]:
        X__ = data__[ 'x' ]
        if nXvars_ is None: nXvars_ = len( X__ )
        
        Q2__ = X__[ 0 ][ 'value' ]
        if Q2__ == '-': continue
        Q2__ = float( Q2__ )
        x__ = float( X__[ 1 ][ 'value' ] )
        y__ = float( X__[ 2 ][ 'value' ] )
        
        Y__ = data__[ 'y' ]
        Y_var__ = Y__[ idx_col_var_ - nXvars_ ]
        val__ = Y_var__[ 'value' ]
        if val__ != '-':
            val__ = float( val__ )
            arr_Q2_.append( Q2__ )
            arr_x_.append( x__ )
            arr_y_.append( y__ )
            arr_val_.append( val__ )
            for err___ in Y_var__[ 'errors' ]:
                errlabel___ = err___[ 'label' ]
                errval___ = float( err___[ 'symerror' ] )
                if errlabel___ not in arr_err_: arr_err_[ errlabel___ ] = []
                arr_err_[ errlabel___ ].append( errval___ )
            
            str__ = ""
            str__ += "{}, {}, {}".format( Q2__, x__, y__ )
            str__ += ", {} = {}".format( varname_, val__ )
            for label___ in arr_err_: str__ += ", {} = {}".format( label___, arr_err_[ label___ ][ -1 ] )
            print ( str__ )
    
    df_ = pd.DataFrame( { 'Q2': arr_Q2_, 'x': arr_x_, 'y': arr_y_, varname_: arr_val_, **arr_err_ } )
    return df_