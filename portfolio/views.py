try: import simplejson as json
except ImportError: import json
import xlwt
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from portfolio.forms import PortfolioForm
from portfolio.models import Portfolio
from rest_framework import generics
from .serializers import PortfolioSerializer


@login_required
def watch_list(request):
    user = request.user
    portfolio = Portfolio.objects.get(user=user)
    print(portfolio)
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol'].upper()
            if not portfolio.lookupStock(symbol):
                portfolio.addStock(symbol)
    form = PortfolioForm()
    infos = portfolio.currentInfo()

    return render(request, 'stocks/watch_list.html', {'form': form,
                                                     'infos': infos})


@login_required
def delete_stock(request, pk):
    stocks = Stock.objects.filter(pk=pk)
    stocks and stocks[0].delete()
    return HttpResponseRedirect(reverse('watch_list'))


@login_required
def historical(request):
    form = StockForm()
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol'].upper()
            data = get_current_info(symbol)
            book = xlwt.Workbook()
            sheet = book.add_sheet('Sheet')
            for i, v in enumerate(data[0].keys()):
                sheet.write(0, i, v)
            for i, row in enumerate(data, start=1):
                for j, v in enumerate(row.values()):
                    sheet.write(i, j, v)
            response = HttpResponse(content_type='application/x-msexcel')
            response['Pragma'] = 'no-cache'
            response['Content-disposition'] = 'attachment; filename=history.xls'
            book.save(response)
            return response

    return render(request, 'stocks/historical.html', {'form': form})


@login_required
def plot(request):
    rows = []
    symbols = Stock.objects.filter(user=request.user).values_list('symbol',
                                                                  flat=True)
    if symbols:
        data = []
        values = []
        for s in symbols:
            history_for_symbol = get_month_info(s)
            history_for_symbol.reverse()
            data.append(history_for_symbol)
            values.append(1000)
        days = [d['Date'] for d in data[0]]
        closes = []
        keys = ['High', 'Low', 'AdjClose']
        for i, day in enumerate(days):
            row = {'Value': 0, 'Date': day, 'Percent': 0, 'Volume': 0,
                   'High': 0, 'Low': 0, 'AdjClose': 0}
            if i == 0:
                for history in data:
                    closes.append(float(history[i]['AdjClose']))
            else:
                for j, history in enumerate(data):
                    ratio = (closes[j] / 100)
                    current_close = float(history[i]['AdjClose'])
                    percent = (current_close - closes[j]) / ratio
                    closes[j] = float(history[i]['AdjClose'])
                    if i > 1:
                        values[j] += values[j] * (percent / 100)
                    row['Value'] += values[j]
                    row['Percent'] += percent
                    row['Volume'] += float(history[i]['Volume'])
                    for k in keys:
                        row[k] += float(history[i][k])
                row['Percent'] /= len(data)
                for k in keys:
                    row[k] /= len(data)
                rows.append(row)
        rows.reverse()
    return render(request, 'stocks/plot.html', {'rows': rows})




class PortfolioAPI(generics.ListCreateAPIView):

    serializer_class = PortfolioSerializer
    #queryset = Stock.objects.all()
    queryset = []
    def perform_create(self, serializer):
        serializer.save()
