from .status import ORDER_FOUND, ORDER_NOT_FOUND, INVALID_AMOUNT


class ClickUz:
    ORDER_FOUND = ORDER_FOUND
    ORDER_NOT_FOUND = ORDER_NOT_FOUND
    INVALID_AMOUNT = INVALID_AMOUNT

    def check_order(self, order_id: str, amount: str):
        """
        :Need to check order
        :param order_id:
        :param amount:
        :return: ORDER_NOT_FOUND or ORDER_FOUND or INVALID_AMOUNT
        """
        raise NotImplemented

    def successfully_payment(self, order_id: str, transaction: object):
        """

        :param order_id:
        :return:
        """
        raise NotImplemented

    def cancel_payment(self, order_id: str, transaction: object):
        """
        ru: еще не добавлено отменить транзакцию
        en: not yet added cancel transaction
        :param order_id:
        :param transaction:
        :return:
        """
        pass
