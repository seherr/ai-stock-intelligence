

def calculate_percentage_change(today_price, yesterday_price):
    """
    Bugünkü fiyat ile dünkü fiyat arasındaki yüzde değişimi hesaplar.

    Formula:
    ((today - yesterday) / yesterday) * 100
    """

    if yesterday_price == 0:
        return 0

    return ((today_price - yesterday_price) / yesterday_price) * 100