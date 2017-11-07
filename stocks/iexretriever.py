import sys
import urllib.parse
try: import simplejson as json
except ImportError: import json

import pandas as pd
import requests
import logging
logging.basicConfig(level=logging.DEBUG)
import datetime

from pandas.tseries.offsets import BDay


today = datetime.date.today() + datetime.timedelta(-1)
last_month = datetime.date.today() + datetime.timedelta(-30)
yesterday = pd.datetime.today() + BDay(-1)
last_year = datetime.date.today() + datetime.timedelta(-365)


class IEXRetriever:

    _IEX_API_URL = "https://api.iextrading.com/1.0/"

    def __init__(self, retries=5, output_format='json', treat_info_as_error=True):

        self.retries = retries
        self.output_format = output_format
        self.treat_info_as_error = treat_info_as_error


    def _validate_response(self, queryfields):
        pass
    #@_retry
    def executeIEXQuery(self, queryfields):
        
        symbols = ','.join(queryfields["symbols"])
        #types= ','.join(queryfields["types"])
        url = (self._IEX_API_URL + '?' +  'symbols=' + symbols + '&types=' + queryfields["types"])
        def _api_call(self, url):
            try:
                r = requests.get(url=url)
                r.raise_for_status
            except requests.exceptions.Timeout:
                pass
            except requests.exceptions.TooManyRedirects:
                pass
            except requests.exceptions.RequestException as e:
                pass
            json_response = r.json()
            return _validate_response(self, queryfields)
        return _api_call(self, url)


    @classmethod
    def _output_format(cls, func, override=None):
        """ Decorator in charge of giving the output its right format, either
        json or pandas
        Keyword Arguments:
            func:  The function to be decorated
            override:  Override the internal format of the call, default None
        """  
        @wraps(func)
        def _format_wrapper(self, *args, **kwargs):
            json_response, data_key, meta_data_key = func(
                self, *args, **kwargs)
            data = json_response[data_key]
            if meta_data_key is not None:
                meta_data = json_response[meta_data_key]
            else:
                meta_data = None
            # Allow to override the output parameter in the call
            if override is None:
                output_format = self.output_format.lower()
            elif 'json' or 'pandas' in override.lower():
                output_format = override.lower()
            # Choose output format
            if output_format == 'json':
                return data, meta_data
            elif output_format == 'pandas':
                data_pandas = pandas.DataFrame.from_dict(data,
                                                         orient='index',
                                                         dtype=float)
                data_pandas.index.name = 'Date'
                # Rename columns to have a nicer name
                col_names = [re.sub(r'\d+.', '', name).strip(' ')
                             for name in list(data_pandas)]
                data_pandas.columns = col_names
                return data_pandas, meta_data
            else:
                raise ValueError('Format: {} is not supported'.format(
                    self.output_format))
        return _format_wrapper

    def _retry(func):
        """ Decorator for retrying api calls (in case of errors from the api
        side in bringing the data)
        Keyword Arguments:
            func:  The function to be retried
        """
        @wraps(func)
        def _retry_wrapper(self, *args, **kwargs):
            error_message = ""
            for retry in range(self.retries + 1):
                try:
                    return func(self, *args, **kwargs)
                except ValueError as err:
                    error_message = str(err)
            raise ValueError(str(error_message))
        return _retry_wrapper

    @staticmethod
    def get_quote(symbol):
        pass

    @staticmethod
    def get_chart(self, symbol):
        pass




def main():
    iexr = IEXRetriever()
    q= {
    "symbols" : ['tsla', 'aapl', 'msft', 'xpo', 'uvxy', 'uso'],
    "types" : 'price',
    }
    hmm = iexr.executeIEXQuery(q)
    print(hmm)
    exit()


if __name__ == "__main__":
    main()