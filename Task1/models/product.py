# product.py
class Product:
    """产品基类，封装通用属性和方法"""
    def __init__(self, product_id: str, name: str, price: float, quantity: int):
        self._product_id = product_id      # 封装：受保护属性
        self._name = name
        self._price = price
        self._quantity = quantity

    # 封装：通过 getter/setter 访问私有属性
    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("价格不能为负数")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("数量不能为负数")
        self._quantity = value

    def get_info(self):
        """获取产品信息（可被子类重写实现多态）"""
        return f"产品ID: {self._product_id}, 名称: {self._name}, 价格: {self._price}, 库存: {self._quantity}"

    def __str__(self):
        return self.get_info()


class ElectronicProduct(Product):
    """电子产品子类，继承 Product"""
    def __init__(self, product_id: str, name: str, price: float, quantity: int, warranty_months: int):
        super().__init__(product_id, name, price, quantity)
        self._warranty_months = warranty_months

    @property
    def warranty_months(self):
        return self._warranty_months

    def get_info(self):
        """重写父类方法，体现多态"""
        base_info = super().get_info()
        return f"{base_info}, 保修期: {self._warranty_months} 个月"


class FoodProduct(Product):
    """食品子类，继承 Product"""
    def __init__(self, product_id: str, name: str, price: float, quantity: int, expiry_date: str):
        super().__init__(product_id, name, price, quantity)
        self._expiry_date = expiry_date

    @property
    def expiry_date(self):
        return self._expiry_date

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, 过期日期: {self._expiry_date}"
