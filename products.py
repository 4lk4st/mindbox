import os
import sys
from pyspark.sql import SparkSession

# Задаем переменные среды для корректного запуска PYSPARK
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
spark = SparkSession.builder.getOrCreate()

# Задаем тестовый датасет
product_df = spark.createDataFrame([
    (1, "Apple"),
    (2, "Orange"),
    (3, "Potato"),
    (4, "Banana")
], schema = "product_id long, product_name string")

category_df = spark.createDataFrame([
    (1, "Fruits"),
    (2, "Vegatables"),
    (3, "Yammies"),
], schema = "category_id long, category_name string")

product_category_df = spark.createDataFrame([
    (1, 1),
    (2, 1),
    (2, 3),
    (3, 2)
], schema = "product_id long, category_id long")

# Итоговый запрос
(product_df
 .join(
    product_category_df,
    product_df.product_id == product_category_df.product_id,
    "left")
 .join(
     category_df,
     product_category_df.category_id == category_df.category_id,
     "left")
.select("product_name", "category_name")
.orderBy("product_name")
.show(truncate=False))

'''
Вывод:
+------------+-------------+
|product_name|category_name|
+------------+-------------+
|Apple       |Fruits       |
|Banana      |NULL         |
|Orange      |Fruits       |
|Orange      |Yammies      |
|Potato      |Vegatables   |
+------------+-------------+
'''