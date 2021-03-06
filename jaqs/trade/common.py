# encoding: UTF-8
from enum import Enum, unique


class ReprEnum(Enum):
    def __repr__(self):
        return "{0:s}_{1:s}".format(self.__class__.__name__,
                                    self._name_)
    
    def __str__(self):
        return "{0:s}_{1:s}".format(self.__class__.__name__,
                                    self._name_)
    
    @property
    def full_name(self):
        return str(self)
    
    @classmethod
    def to_enum(cls, key):
        return cls.__members__.get(key.upper(), None)


class ReprIntEnum(int, ReprEnum):
    """Enum where members are also (and must be) ints"""
    pass


class ReprStrEnum(str, ReprEnum):
    """Enum where members are also (and must be) ints"""
    pass


@unique
class QUOTE_TYPE(ReprStrEnum):
    TICK = '0'
    MIN = '1M'
    FIVEMIN = '5M'
    QUARTERMIN = '15M'
    DAILY = '1d'
    SPECIALBAR = '-1'
    # %Y%m%d%H%M%S


@unique
class RUN_MODE(ReprIntEnum):
    REALTIME = 0
    BACKTEST = 1


@unique
class EXCHANGE(ReprStrEnum):
    SHENZHEN_STOCK_EXCHANGE = 'SZ'
    SHANGHAI_STOCK_EXCHANGE = 'SH'
    
    SHANGHAI_FUTURES_EXCHANGE = 'SHF'
    ZHENGZHOU_COMMODITIES_EXCHANGE = 'CZC'
    DALIAN_COMMODITIES_EXCHANGE = 'DCE'
    
    CHINA_FINANCIAL_FUTURES_EXCHANGE = 'CFE'
    
    SHANGHAI_GOLD_EXCHANGE = 'SGE'
    
    CHINA_SECURITY_INDEX = 'CSI'
    
    HONGKONG_EXCHANGES_AND_CLEARING_LIMITED = 'HK'


@unique
class ORDER_TYPE(ReprStrEnum):
    """We recommend use limit order everywhere."""
    MARKET = "market"
    LIMIT = "limit"
    STOP = "stop"  # convert to market order once symbol price meet certain conditions.
    VWAP = "vwap"
    


@unique
class ORDER_ACTION(ReprStrEnum):
    """
    buy and sell for long; short and cover for short.
    other 4 actions are automatically generated by EMS."""
    BUY = "Buy"
    SELL = "Sell"
    SHORT = "Short"
    COVER = "Cover"
    SELLTODAY = "SellToday"
    SELLYESTERDAY = "SellYesterday"
    COVERYESTERDAY = "CoverYesterday"
    COVERTODAY = "CoverToday"
    
    @classmethod
    def is_positive(cls, action):
        return (action == cls.BUY
                or action == cls.COVER
                or action == cls.COVERYESTERDAY
                or action == cls.COVERTODAY)

    @classmethod
    def is_negative(cls, action):
        return (action == cls.SELL
                or action == cls.SHORT
                or action == cls.SELLTODAY
                or action == cls.SELLYESTERDAY)


@unique
class ORDER_STATUS(ReprStrEnum):
    NEW = "New"
    REJECTED = "Rejected"
    ACCEPTED = "Accepted"
    FILLED = "Filled"
    CANCELLED = "Cancelled"


@unique
class TASK_STATUS(ReprStrEnum):
    NEW = "New"
    REJECTED = "Rejected"
    ACCEPTED = "Accepted"
    DONE = "Done"
    CANCELLED = "Cancelled"


@unique
class ORDER_TIME_IN_FORCE(ReprStrEnum):
    FOK = 'fok'
    FAK = 'fak'
    IOC = 'ioc'


@unique
class CALENDAR_CONST(ReprIntEnum):
    TRADE_DAYS_PER_YEAR = 242


if __name__ == "__main__":
    """What below are actually unit tests. """
    
    print "Running test..."
    
    assert QUOTE_TYPE.TICK == '0'
    assert RUN_MODE.BACKTEST == 1
    assert ORDER_ACTION.BUY == 'Buy'
    assert ORDER_TYPE.MARKET == 'market'
    assert ORDER_STATUS.FILLED == 'Filled'
    
    print "Test passed."
