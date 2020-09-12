from simulator.active_customers import ActiveCustomers
import settings

if __name__ == '__main__':
    output = ActiveCustomers(settings.periods).save_activity_table_to_csv()