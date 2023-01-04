import pandas as pd

def get_df_json_CMS_QCD( json_data ):

    Xvars_ = (0,1,2)
    
    arr_X_low_ = []
    arr_X_high_ = []
    arr_val_ = []
    arr_err_ = {}
    
    column_names_ = []
    idx_col_var_ = None
    for idx__,data__ in enumerate( json_data[ 'headers' ] ):
        name__ = data__[ 'name' ]
        column_names_.append( data__[ 'name' ] )
    print ( column_names_ )
    
    for data__ in json_data[ 'values' ]:
        X__ = data__[ 'x' ][ 0 ]
        X_low__  = float( X__[ 'low' ] )
        X_high__ = float( X__[ 'high' ] )
        
        Y__ = data__[ 'y' ][ 0 ]
        val__ = float( Y__[ 'value' ] )
        arr_X_low_.append( X_low__ )
        arr_X_high_.append( X_high__ )
        arr_val_.append( val__ )
        for err___ in Y__[ 'errors' ]:
            errlabel___ = err___[ 'label' ]
            errval___ = abs( float( err___[ 'symerror' ] ) )
            if errlabel___ not in arr_err_: arr_err_[ errlabel___ ] = []
            arr_err_[ errlabel___ ].append( errval___ )
            
        str__ = ""
        str__ += "{}, {}, {}".format( arr_X_low_[ -1 ], arr_X_high_[ -1 ], arr_val_[ -1 ] )
        for label___ in arr_err_: str__ += " ±{} ({})".format( arr_err_[ label___ ][ -1 ], label___ )
        print ( str__ )
    
    df_ = pd.DataFrame( { 'X_low': arr_X_low_, 'X_high': arr_X_high_, 'val': arr_val_, **arr_err_ } )
    return df_