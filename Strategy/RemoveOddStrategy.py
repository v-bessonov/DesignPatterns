from Strategy.FilterStrategy import FilterStrategy


class RemoveOddStrategy(FilterStrategy):
    def remove_values(self, val):
        return abs(val) % 2
