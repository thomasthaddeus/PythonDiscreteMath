"""16.8 LAB*: Program: Automobile service invoice."""

cost1 = []
def service_1(service1):
    """Car service number 1."""
    service_cost_1 = {'oil_change': int(35), 'tire_rotation': int(19), 'car_wash': int(7), 'car_wax': int(12)}
    if service1 == 'Oil change':
        cost1.append(int(35))
        print(f"Service 1: {service1}, ${service_cost_1['oil_change']}")
    elif service1 == 'Tire rotation':
        cost1.append(int(19))
        print(f"Service 1: {service1}, ${service_cost_1['tire_rotation']}")
    elif service1 == 'Car wash':
        cost1.append(int(7))
        print(f"Service 1: {service1}, ${service_cost_1['car_wash']}")
    elif service1 == 'Car wax':
        cost1.append(int(12))
        print(f"Service 1: {service1}, ${service_cost_1['car_wax']}")
    elif service1 == '-':
        cost1.append(int(0))
        print("Service 1: No service")
    return cost1

cost2 = []
def service_2(service2):
    """Second car service."""
    service_cost_2 = {'oil_change': int(35), 'tire_rotation': int(19), 'car_wash': int(7), 'car_wax': int(12)}
    if service2 == 'Oil change':
        cost2.append(int(35))
        print(f"Service 2: {service2}, ${service_cost_2['oil_change']}")
    elif service2 == 'Tire rotation':
        cost2.append(int(19))
        print(f"Service 2: {service2}, ${service_cost_2['tire_rotation']}")
    elif service2 == 'Car wash':
        cost2.append(int(7))
        print(f"Service 2: {service2}, ${service_cost_2['car_wash']}")
    elif service2 == 'Car wax':
        cost2.append(int(12))
        print(f"Service 2: {service2}, ${service_cost_2['car_wax']}")
    elif service2 == '-':
        print("Service 2: No service")
        cost2.append(int(0))
    return cost2


print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")
print("Select first service:")
print("Select second service:\n")

service1 = input()
service2 = input()

print("Davy's auto shop invoice\n")

service_1(service1)
service_2(service2)

total = [x + y for x, y in zip(cost1, cost2)]
print(f"\nTotal: ${total[0]}")
