class TrackOrders:
    def __init__(self) -> None:
        self._orders = list()

    def __len__(self):
        return len(self._orders)

    def add_new_order(self, customer, order, day):
        return self._orders.append({
            "customer": customer,
            "order": order,
            "day": day
        })

    def get_most_ordered_dish_per_customer(self, customer):
        order_list = [
            order["order"] for order in self._orders
            if order["customer"] == customer
        ]

        order_count = dict()
        most_ordered = order_list[0]

        for order in order_list:
            if order not in order_count:
                order_count[order] = 1
            else:
                order_count[order] += 1

            if order_count[order] > order_count[most_ordered]:
                most_ordered = order

        return most_ordered

    def get_never_ordered_per_customer(self, customer):
        customer_orders = set()
        order_set = set()

        for order in self._orders:
            order_set.add(order["order"])

            if order["customer"] == customer:
                customer_orders.add(order["order"])

        return order_set.difference(customer_orders)

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        customer_days = set()

        for order in self._orders:
            days.add(order["day"])

            if order["customer"] == customer:
                customer_days.add(order["day"])

        return days.difference(customer_days)

    def get_busiest_day(self):
        days_list = [order["day"] for order in self._orders]

        days_count = dict()
        most_busy = days_list[0]

        for day in days_list:
            if day not in days_count:
                days_count[day] = 1
            else:
                days_count[day] += 1

            if days_count[day] > days_count[most_busy]:
                most_busy = day

        return most_busy

    def get_least_busy_day(self):
        days_list = [order["day"] for order in self._orders]

        days_count = dict()
        least_busy = days_list[0]

        for day in days_list:
            if day not in days_count:
                days_count[day] = 1
            else:
                days_count[day] += 1

            if days_count[day] < days_count[least_busy]:
                least_busy = day

        return least_busy
