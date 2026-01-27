from langchain_community.utilities.polygon import PolygonAPIWrapper
from langchain_community.tools import (
    PolygonLastQuote,
    PolygonTickerNews,
    PolygonFinancials,
    PolygonAggregates,
)
from ..config import Settings

def make_polygon_tools(settings: Settings):
    polygon = PolygonAPIWrapper(api_key=settings.polygon_api_key)
    return [
        PolygonLastQuote(api_wrapper=polygon),
        PolygonTickerNews(api_wrapper=polygon),
        PolygonFinancials(api_wrapper=polygon),
        PolygonAggregates(api_wrapper=polygon),
    ]
