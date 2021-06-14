from ecommerce.controllers import Controller
from ecommerce.databases.models.category import Category


class CategoryController(Controller):
    def __init__(self):
        self.category = Category()

    def index(self):
        categories = self.category.find()
        for category in categories:
            print(category)
        return categories

    def top_3_categories(self):
        categories = self.category.aggregate([{'$limit': 3}])
        return categories



    # =======================method to return parent and child category name============================
    def product_category(self):
        product_categories = self.category.aggregate([
            {
                "$match": {"parent_category_id": None}
            },
            {
                "$lookup":
                    {
                        "from": 'Product_Category',
                        "localField": 'product_category_id',
                        "foreignField": 'parent_category_id',
                        "as": 'child_categories'
                    }
            }
        ])
        return product_categories


        #    =========================first solution==========================
        # return product_child_categories.aggregate([
        #         {
        #             "$project": {
        #                 # "_id": NumberInt(0),
        #                 "s1": "$$ROOT"
        #             }
        #         },
        #         {
        #             "$lookup": {
        #                 "localField": "s1.product_category_id",
        #                 "from": "category_controller",
        #                 "foreignField": "parent_category_id",
        #                 "as": "child_category"
        #             }
        #         },
        #         {
        #             "$unwind": {
        #                 "path": "$child_category",
        #                 "preserveNullAndEmptyArrays": "true"
        #             }
        #         },
        #         {
        #             "$match": {
        #                 "s1.parent_category_id": {
        #                     "$eq": "null"
        #                 }
        #             }
        #         },
        #         {
        #             "$project": {
        #                 "s1._id": "$s1._id",
        #                 "s1.product_category_id": "$s1.product_category_id",
        #                 "s1.product_category_name": "$s1.product_category_name",
        #                 "child_category._id": "$child_category._id",
        #                 "child_category.product_category_id": "$child_category.product_category_id",
        #                 "child_category.product_category_name": "$child_category.product_category_name",
        #                 "child_category.product_Category_image_path": "$child_category.product_Category_image_path",
        #                 "child_category.parent_category_id": "$child_category.parent_category_id",
        #                 # "_id": NumberInt(0)
        #             }
        #         }
        #     ]
        #     # {
        #     #     "allowDiskUse": true
        #     # }
        # )
