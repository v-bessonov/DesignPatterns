from Strategy.FilterStrategy import FilterStrategy


class RemoveNegativeStrategy(FilterStrategy):
    def remove_values(self, val):
        return val < 0
