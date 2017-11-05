try:
  import unzip_requirements
except ImportError:
  pass

import matplotlib
matplotlib.use('Agg')

import logging
import json 
import pandas as pd
import numpy as np
from fbprophet import Prophet


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def prophet_test():
    df = pd.DataFrame()
    df['ds'] = pd.date_range('1/1/2011', periods=24, freq='H')
    df['y'] = pd.Series(np.random.randn(len(df)))
    df['y'] = np.log(df['y'].abs())
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=10)
    return m.predict(future)


def lambda_test(event=None, context=None):
    logger.info('Lambda test')
    result_df = prophet_test()
    return {'statusCode': 200,
            'body': result_df.to_json()}
