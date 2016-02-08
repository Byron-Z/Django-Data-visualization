import datetime
import json
import requests
from client.models import *
from django.core.exceptions import ObjectDoesNotExist

class FetchJob():
    """

    Grabs data from the server and puts it in the database. This class is
    instantiated/run periodically at an interval defined in fetchdata.py. Feel
    free to check out the fetchdata command (in client/management/commands).
    The API response formats are in the README. Be sure to handle both the
    creation of new companies/metrics and the updating of existing ones. Be
    mindful of foreign key dependencies.

    """

    def run(self):
        """

        Entry point for the FetchJob class. This should grab data from the
        API and put it into the database.
        """
        #Get companies information and store them into database
        raw_company_data = requests.get('http://investmentiq.herokuapp.com/api/v1/companies/')
        company_data = json.loads(raw_company_data.text)
        for company in company_data:
            try:
                com = Company.objects.get(name=company['name'])
                com.founded = company['founded']
                com.series = company['series']
                com.valuation = company['valuation']
                com.description = company['description']
                com.save()
            except ObjectDoesNotExist:
                Company.objects.create(name=company['name'],founded = company['founded'],
                        series = company['series'], valuation = company['valuation'], description = company['description'])
        
        #Get metrics information and store them into database
        raw_metric_data = requests.get('http://investmentiq.herokuapp.com/api/v1/metrics/rand/')
        metric_data = json.loads(raw_metric_data.text)
        for metric in metric_data:
            com_name = Company.objects.get(name=metric['company'])
            try:
                met = Metric.objects.get(company=com_name, name=metric['name'])
                met.start_date = metric['start_date']
                met.end_date = metric['end_date']
                met.value = metric['value']
                met.save()
            except ObjectDoesNotExist:
                Metric.objects.create(name=metric['name'], start_date = metric['start_date'], 
                    end_date = metric['end_date'], value = metric['value'], company=com_name)

        return
