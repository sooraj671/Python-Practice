from ecommerce.shopping.module_sale import cal_shipping, cal_tax
# import module_sale
cal_shipping()
# module_sale.cal_tax()

from ecommerce.customer import contact
# from ..customer import contact

from ecommerce.shopping import module_sale
print(dir(contact))

print(contact.__name__)
print(contact.__package__)
print(contact.__file__)

