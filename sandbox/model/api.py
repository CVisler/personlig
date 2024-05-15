from models import Construct

actuals = Construct(table='actuals')
sst = Construct(table='sst')
orders = Construct(table='orders')

print(actuals.model_dump_json(indent=4))
print(sst.model_dump_json(indent=4))
print(orders.model_dump_json(indent=4))
