def get_non_compliant_days_by_limit(self):
        """
        Returns non-compliant days grouped by limit category.
        """
        non_compliant_days = self.get_non_compliant_days()
        grouped_days = {}

        for day in non_compliant_days:
            limit_category = day['limit_category']  # Assumed the structure of the data
            if limit_category not in grouped_days:
                grouped_days[limit_category] = []
            grouped_days[limit_category].append(day)

        return grouped_days
