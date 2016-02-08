from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.core import serializers

from client.models import Company, Metric

class ClientViews:
    """
    Provides view-based endpoints that serve static files. The data are loaded
    asynchronously by the client (see the JS files in the scripts directory)
    instead of preloaded into the DOM via Python's templating engine.
    See urls.py for the URL mappings.

    """

    @classmethod
    def companies(cls, request):
        return render_to_response('views/companies.html')

    @classmethod
    def company(cls, request, company_name):
        return render_to_response('views/company.html', {'cname': company_name})

    @classmethod
    def metrics(cls, request):
        return render_to_response('views/metrics.html')

class ClientAPI:
    """

    Implements internal API endpoints, which expose data to the client. In
    order to properly connect with the provided client code, the JsonResponse
    objects you return should *exactly* follow the format in the method
    docstrings. 
    """

    @classmethod
    def _serialize(cls, objects):
        def create_company_map():
            return {c.id: c.name for c in Company.objects.all()}

        # Replace company ids with company names
        def map_company(obj, company_map):
            if 'company' in obj:
                obj['company'] = company_map[obj['company']]
            return obj

        company_map = create_company_map()
        raw = serializers.serialize('python', objects)
        res = [dict(map_company(obj['fields'], company_map)) for obj in raw]
        return res

    @classmethod
    def get_companies(cls, request):
        """
        TODO:

        Returns a serialized JsonResponse object of all company data (one
        dictionary hash per company for each company in the database).

        @return [JsonReponse]: [{
            "founded": "2000-01-01",
            "name": "MyCo1",
            "series": "Series A",
            "valuation": "123456789.00",
            "description": "MyCo1 is making the world a better place..."
        }, {
            "founded": "2001-01-01",
            "name": "MyCo2",
            "series": "Series B",
            "valuation": "987654321.00",
            "id": 2,
            "description": "MyCo2 is making the world a better place..."
        },
        ...
        ]
        """
        res = ClientAPI._serialize(Company.objects.all())
        return JsonResponse(res, safe=False)

    @classmethod
    def get_company(cls, request, company_name):
        """
        TODO:

        Returns a serialized JsonResponse object of company data for a company
        with id @company_id (a list of one element - a single dictionary hash
        for the queried company, or an empty list if no companies are found).
        NOTE: This returns a JSON-encoded list, not a JSON-encoded dict.

        @return [JsonReponse]: [{
            "name": "MyCo1",
            "founded": "2000-01-01",
            "series": "Series A",
            "valuation": "123456789.00",
            "description": "MyCo1 is making the world a better place..."
        }]
        """

        res = ClientAPI._serialize(Company.objects.filter(id=company_name))
        return JsonResponse(res, safe=False)

    @classmethod
    def get_metrics(cls, request):
        """
        TODO:

        Returns a serialized JsonResponse object of all metric data (one
        dictionary hash for each metric in the database).
        NOTE: Be sure to order metrics by date in your response!

        @return [JsonReponse]: [{
            "company": "MyCo1",
            "name": "Cash Burn",
            "start_date": "2000-01-01",
            "end_date": "2000-03-31",
            "value": -10000.0,
        }, {
            "company": "MyCo2",
            "name": "Cash Burn",
            "start_date": "2000-01-01",
            "end_date": "2000-03-31",
            "value": -20000.0},
        },
        ...
        ]
        """
        res = ClientAPI._serialize(Metric.objects.all())
        return JsonResponse(res, safe=False)

    @classmethod
    def get_metrics_by_company(cls, request, company_name):
        """
        TODO:

        Returns a serialized JsonResponse object of all metric data for a
        single company with id @company_id (one dictionary hash for each metric
        in the database relating to that company - company 1 in the example
        below).
        NOTE: Be sure to order metrics by date in your response!

        @return [JsonReponse]: [{
            "company": "MyCo1",
            "name": "Cash Burn",
            "start_date": "2000-01-01",
            "end_date": "2000-03-31",
            "value": -10000.0,
        }, {
            "company": "MyCo2",
            "name": "Headcount",
            "start_date": "2000-01-01",
            "end_date": "2000-03-31",
            "value": 100.0},
        },
        ...
        ]
        """
        company_id = Company.objects.get(name=company_name)
        res = ClientAPI._serialize(Metric.objects.filter(company=company_id))
        return JsonResponse(res, safe=False)
