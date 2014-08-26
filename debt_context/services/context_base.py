class ContextBase:
    def population_context(self):
        return self.hashify(self.context_population())

    def assessed_valuation(self):
        return self.hashify(self.context_assessed_valuation())

    def tax_debt_per_capita(self):
        return self.hashify(self.context_tax_debt_per_capita())

    def hashify(self, context):
        # If there is no context, will return an empty Array
        if len(context) == 1:
            return []
        else:
            return [entity.to_short_dict() for entity in context]

