# inventory.py
from typing import Dict, List
from .product import Product
from .category import Category

class Inventory:
    """库存管理系统主类"""
    def __init__(self):
        self._products: Dict[str, Product] = {}      # 产品ID -> 产品对象
        self._categories: Dict[str, Category] = {}   # 类别名 -> 类别对象

    def add_product(self, product: Product, category_name: str = "未分类"):
        """添加产品到库存，并归类"""
        if product.product_id in self._products:
            raise ValueError("产品ID已存在")
        self._products[product.product_id] = product

        # 确保类别存在
        if category_name not in self._categories:
            self._categories[category_name] = Category(category_name)
        self._categories[category_name].add_product(product)

    def remove_product(self, product_id: str):
        """从库存移除产品"""
        if product_id not in self._products:
            raise ValueError("产品不存在")
        product = self._products.pop(product_id)
        # 从所属类别中移除（简化：遍历所有类别删除）
        for category in self._categories.values():
            category.remove_product(product_id)

    def search_by_id(self, product_id: str):
        return self._products.get(product_id)

    def search_by_name(self, keyword: str):
        result = []
        for p in self._products.values():
            if keyword.lower() in p.name.lower():
                result.append(p.get_info())
        return result

    def get_all_products(self):
        return [p.get_info() for p in self._products.values()]

    def __str__(self):
        return f"库存管理系统 - 共有 {len(self._products)} 个产品，{len(self._categories)} 个类别"
