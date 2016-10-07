import pandas as pd

from django.core.exceptions import ValidationError

VALID_CORRELATION_METHODS = ['pearson', 'spearman', 'kendall']


class DataFrameEventsAnalyzer(object):
    """
    Takes a DataFrame and returns analytics on top of it.
    """
    def __init__(self, dataframe, ignore_columns=None, rest_day_column_name=None):
        # certain columns might be just notes or useless information that can be ignored
        if ignore_columns:
            assert isinstance(ignore_columns, list)
            self.ignore_columns = ignore_columns
        else:
            self.ignore_columns = []

        # if it's a rest day, the correlations shouldn't be used. ie. if you're drinking caffeine on
        # Sunday and wasn't intending to get any work done, then those days shouldn't be used to measure how effective
        # caffeine is.
        if rest_day_column_name:
            assert isinstance(rest_day_column_name, str)
            dataframe = dataframe[dataframe[rest_day_column_name] == False]  # noqa

        dataframe_cols = dataframe.columns
        valid_columns = [item for item in dataframe_cols if item not in ignore_columns]

        self.valid_columns = valid_columns
        self.dataframe = dataframe

    @staticmethod
    def _add_yesterday_correlation_to_dataframe(dataframe, valid_columns):
        for col in valid_columns:
            # Advil - Yesterday
            shifted_col_name = '{0} - Yesterday'.format(col)
            series = dataframe[col]
            shifted_series = series.shift(1)
            dataframe[shifted_col_name] = shifted_series

        return dataframe

    def get_correlation_for_measurement(self, measurement, add_yesterday_lag=False, method='pearson', min_periods=1):
        """
        IE. Measurement is the column name of what you're trying to improve / correlate
        If add_yesterday_lag is True, take a look if yesterday's supplements impacted
        Productivity / Sleep / etc. today.
        """
        self._validate_correlation_method(method)
        # copy lets me be certain each result doesn't mess up state
        dataframe = self.dataframe.copy()

        if add_yesterday_lag:
            dataframe = self._add_yesterday_correlation_to_dataframe(dataframe)

        dataframe = self._remove_invalid_measurement_days(dataframe)

        correlation_results = dataframe.corr(method, min_periods)[measurement]
        correlation_results_sorted = correlation_results.sort_values(inplace=False)

        return correlation_results_sorted

    def get_rolling_correlation_for_measurement(self, measurement, window, method='pearson', min_periods=1):
        self._validate_correlation_method(method)
        # copy lets me be certain each result doesn't mess up state
        dataframe = self.dataframe.copy()

        dataframe = self._remove_invalid_measurement_days(dataframe)
        # kind of an annoying internal debate, but theoretically for pearson (i can't verify for all)
        # the sum of a lookback, ie. let's say you took
        # day (x-axis)  | caffeine  | theanine  | productive time
        # 0             | 100mg     | 0 mg      | 20m
        # 1             | 50        | 0 mg      | 10m
        # 2             | 150       | 0 mg      | 25m
        # 3             | 100       | 100 mg    | 60m
        # the sum versus average over a rolling period SHOULD result in the sme correlation
        # should probably check this with a test ...
        dataframe = pd.rolling_sum(dataframe, window=window)

        correlation_results = dataframe.corr(method, min_periods)[measurement]
        correlation_results_sorted = correlation_results.sort_values(inplace=False)

        return correlation_results_sorted

    @staticmethod
    def _remove_invalid_measurement_days(dataframe, measurement):
        """
        if productivity is marked as zero, that shouldn't be used to measure effectiveness
        since it's almost impossible to get a zero using RescueTime as a productive driver
        this might not be the best measurement ... perhaps serializer should just fill with np.NaN
        so when you get the data here you can make a more accurate decision to scrap
        """
        valid_days = dataframe[measurement] != 0
        dataframe = dataframe[valid_days]
        return dataframe

    @staticmethod
    def _validate_correlation_method(method):
        if not isinstance(method, str):
            raise ValidationError('Correlation must be a string')

        if method not in VALID_CORRELATION_METHODS:
            raise ValidationError('Correlation must be one of {0} methods'.format(VALID_CORRELATION_METHODS))
