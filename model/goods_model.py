from dataclasses import dataclass


@dataclass
class GoodsModel:
    goods_id: int
    product_id: int
    name: str
    pic_url: str
    is_new: bool
    is_hot: bool
    counter_price: float
    retail_price: float
