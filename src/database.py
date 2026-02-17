def get_non_compliant_days_by_limit(self):
    non_compliant_days = {}

    # Assuming 'data' is a list of records with 'date' and 'limit' fields
    for record in self.data:
        date = record['date']
        limit = record['limit']

        # Check if the record is non-compliant
        if not self.is_compliant(record):
            if limit not in non_compliant_days:
                non_compliant_days[limit] = []
            non_compliant_days[limit].append(date)

    return non_compliant_days