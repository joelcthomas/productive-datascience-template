"""
AI application to predict the future
"""

def select_data_between_days(data, start_date, end_date):
    """Reads config file from config directory

    Args:
        None

    Returns:
        config
    """
    return data.filter("date between '{}' and '{}'".format(start_date, end_date))