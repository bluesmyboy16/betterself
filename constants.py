# Dataframe Constants
SLEEP_MINUTES_COLUMN = 'Sleep Minutes'

LOOKBACK_PARAM_NAME = 'lookback'

# the sleep cutoff time determines if sleep duration should be calculated for the previous day or next
SLEEP_CUTOFF_TIME = 11
VERY_PRODUCTIVE_TIME_LABEL = 'Very Productive Minutes'
PRODUCTIVE_TIME_LABEL = 'Productive Minutes'
NEUTRAL_TIME_LABEL = 'Neutral Minutes'
DISTRACTING_TIME_LABEL = 'Distracting Minutes'
VERY_DISTRACTING_TIME_LABEL = 'Very Distracting Minutes'
VERY_PRODUCTIVE_MINUTES_VARIABLE = 'very_productive_time_minutes'
PRODUCTIVE_MINUTES_VARIABLE = 'productive_time_minutes'
NEUTRAL_MINUTES_VARIABLE = 'neutral_time_minutes'
DISTRACTING_MINUTES_VARIABLE = 'distracting_time_minutes'
VERY_DISTRACTING_MINUTES_VARIABLE = 'very_distracting_time_minutes'
PRODUCTIVITY_DRIVERS_LABELS = [
    VERY_PRODUCTIVE_TIME_LABEL,
    PRODUCTIVE_TIME_LABEL,
    NEUTRAL_TIME_LABEL,
    DISTRACTING_TIME_LABEL,
    VERY_DISTRACTING_TIME_LABEL,
]
PRODUCTIVITY_DRIVERS_KEYS = [
    VERY_PRODUCTIVE_MINUTES_VARIABLE,
    PRODUCTIVE_MINUTES_VARIABLE,
    NEUTRAL_MINUTES_VARIABLE,
    DISTRACTING_MINUTES_VARIABLE,
    VERY_DISTRACTING_MINUTES_VARIABLE,
]
PRODUCTIVITY_KEYS_TO_LABELS = dict(zip(PRODUCTIVITY_DRIVERS_LABELS, PRODUCTIVITY_DRIVERS_KEYS))
