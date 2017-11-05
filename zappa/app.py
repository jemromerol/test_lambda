import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def lambda_test(event=None, context=None):
    logger.info('Lambda test')
    print "Hello world!"

# import logging
# import pandas as pd
# import numpy as np
# from fbprophet import Prophet
# from flask import Flask 
# from zappa.async import task


# app = Flask(__name__)
# logging.basicConfig()
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)


# #@task
# def lambda_test():
#     df = pd.DataFrame()
#     df['ds'] = pd.date_range('1/1/2011', periods=72, freq='H')
#     df['y'] = pd.Series(np.random.randn(len(df)))
#     df['y'] = np.log(df['y'].abs())
#     m = Prophet()
#     m.fit(df)
#     future = m.make_future_dataframe(periods=365)
#     forecast = m.predict(future)
#     print forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()


# @app.route('/', methods=['GET', 'POST'])
# def test(event=None, context=None):
#     try:
#         lambda_test()
#         return "Ok!"
#     except:
#         return "Failed"


# if __name__ == '__main__':
#     app.run(debug=True)
