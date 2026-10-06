from config import MONTH_NAMES

def get_folder_name(date):
    return (
        f"{date.year}-{date.month:02d} "
        f"{MONTH_NAMES[date.month - 1]}"
    )